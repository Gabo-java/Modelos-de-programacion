#Implementacion del patron de cadena de responsabilidad
#Controla el flujo de turnos de cada jugador 
class ManejadorJugador:
    def __init__(self, jugador):
        self.jugador=jugador
        self.siguiente=None

    def establecer_siguiente(self, siguiente):
        self.siguiente=siguiente
        return siguiente

    def manejar(self, juego):
        if self.jugador["vivo"]:
            juego.turno_actual=self.jugador
            juego.mostrar_mensaje(f"Turno de {self.jugador['nombre']}")
            return self
        elif self.siguiente:
            return self.siguiente.manejar(juego)
        else:
            return None
