"""turno.py
Chain of Responsibility para las fases de turno.
"""

class HandlerTurno:
    def __init__(self, siguiente=None):
        self.siguiente = siguiente

    def manejar(self, contexto: dict):
        raise NotImplementedError

class InicioTurnoHandler(HandlerTurno):
    def manejar(self, contexto: dict):
        jugador = contexto["jugador_actual"]
        modo_avanzado = contexto.get("modo_avanzado", True)
        jugador.iniciar_turno(modo_avanzado)
        if self.siguiente:
            return self.siguiente.manejar(contexto)
        return True

class AccionHandler(HandlerTurno):
    def manejar(self, contexto: dict):
        return False

class FinTurnoHandler(HandlerTurno):
    def manejar(self, contexto: dict):
        jugador = contexto["jugador_actual"]
        modo_avanzado = contexto.get("modo_avanzado", True)
        jugador.finalizar_turno(modo_avanzado)
        if self.siguiente:
            return self.siguiente.manejar(contexto)
        return True

class TurnoManager:
    def __init__(self, jugadores: list, modo_avanzado: bool):
        self.jugadores = jugadores
        self.indice_actual = 0
        self.cadena = InicioTurnoHandler(AccionHandler(FinTurnoHandler()))
        self.turno_actual = self.jugadores[self.indice_actual]
        self.contexto = {"jugador_actual": self.turno_actual, "modo_avanzado": modo_avanzado}
        self.cadena.manejar(self.contexto)

    def obtener_oponente(self):
        return self.jugadores[1 - self.indice_actual]

    def pasar_turno(self):
        self.indice_actual = (self.indice_actual + 1) % len(self.jugadores)
        self.turno_actual = self.jugadores[self.indice_actual]
        self.contexto["jugador_actual"] = self.turno_actual
        self.cadena.manejar(self.contexto)
