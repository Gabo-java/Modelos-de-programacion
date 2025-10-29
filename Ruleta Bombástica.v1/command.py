#Implementacion del patron comando
#Se encarga del manejo de las palancas
class Comando:
    def ejecutar(self):
        pass

class ComandoActivarPalanca(Comando):
    def __init__(self, jugador, indice_palanca, juego):
        self.jugador=jugador
        self.indice_palanca=indice_palanca
        self.juego=juego

    def ejecutar(self):
        return self.juego.activar_palanca(self.jugador, self.indice_palanca)
