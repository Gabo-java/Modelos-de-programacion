"""turno.py
Implementación de Chain of Responsibility para el flujo de turnos.
"""
class HandlerTurno:
    def __init__(self, siguiente=None):
        self.siguiente = siguiente

    def manejar(self, contexto):
        raise NotImplementedError()

class InicioTurnoHandler(HandlerTurno):
    def manejar(self, contexto):
        jugador = contexto['jugador_actual']
        jugador.iniciar_turno()
        if self.siguiente:
            return self.siguiente.manejar(contexto)
        return True

class AccionHandler(HandlerTurno):
    def manejar(self, contexto):
        # Espera la interacción del jugador (UI). No hace auto-progreso.
        return False

class FinTurnoHandler(HandlerTurno):
    def manejar(self, contexto):
        # Comprobaciones posteriores al turno
        if self.siguiente:
            return self.siguiente.manejar(contexto)
        return True

class TurnoManager:
    def __init__(self, jugadores):
        self.jugadores = jugadores
        self.indice_actual = 0
        self.cadena = InicioTurnoHandler(AccionHandler(FinTurnoHandler()))
        self.turno_actual = self.jugadores[self.indice_actual]
        self.contexto = {'jugador_actual': self.turno_actual}
        # iniciar primer turno
        self.cadena.manejar(self.contexto)

    def obtener_oponente(self):
        return self.jugadores[1 - self.indice_actual]

    def siguiente_fase(self):
        # finalizar turno actual y pasar al siguiente
        self._pasar_turno()

    def _pasar_turno(self):
        # mover al siguiente jugador
        self.indice_actual = (self.indice_actual + 1) % len(self.jugadores)
        self.turno_actual = self.jugadores[self.indice_actual]
        self.contexto['jugador_actual'] = self.turno_actual
        # iniciar cadena para el nuevo turno
        self.cadena.manejar(self.contexto)