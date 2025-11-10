"""jugador.py
Clase Jugador que contiene la lógica de dados, rerolls, objetos y vida.
"""
import random
from configuracion import DADOS_INICIALES, MAX_REROLLS_POR_TURNO, VIDA_INICIAL

class Jugador:
    """Representa a un jugador en el juego.

    Atributos principales (nombres en español):
    - nombre
    - vida
    - vida_maxima
    - dados (lista de enteros)
    - rerolls_realizados (int)
    - perder_dados_siguiente_turno (int)
    - cartas (lista de objetos Carta)
    - objetos (lista) -- sistema básico de objetos consumibles
    """
    def __init__(self, nombre, vida_maxima=VIDA_INICIAL, cartas=None):
        self.nombre = nombre
        self.vida = vida_maxima
        self.vida_maxima = vida_maxima
        self.rerolls_realizados = 0
        self.perder_dados_siguiente_turno = 0
        self.cartas = cartas or []
        self.dados = []
        self.objetos = []
        self.iniciar_turno()

    def iniciar_turno(self):
        cantidad = DADOS_INICIALES - self.perder_dados_siguiente_turno
        if cantidad < 1:
            cantidad = 1
        self.dados = [random.randint(1, 6) for _ in range(cantidad)]
        # los rerolls se reinician cada turno
        self.rerolls_realizados = 0
        # resetear perder_dados_siguiente_turno después de aplicarlo
        self.perder_dados_siguiente_turno = 0

    def hacer_reroll(self):
        # Permite hasta MAX_REROLLS_POR_TURNO rerolls en el mismo turno
        if self.rerolls_realizados >= MAX_REROLLS_POR_TURNO:
            return False
        if not self.dados:
            return False
        self.rerolls_realizados += 1
        # Cada reroll suma +1 a todos los dados respecto a la nueva tirada
        self.dados = [max(1, random.randint(1, 6) + self.rerolls_realizados) for _ in range(len(self.dados))]
        # planificar perder dados el siguiente turno (máx 2)
        self.perder_dados_siguiente_turno = min(self.rerolls_realizados, 2)
        return True

    def usar_dado(self, indice):
        """Usa y remueve el dado en la posición indice y devuelve su potencia.
        Si el índice no es válido devuelve None.
        """
        if indice < 0 or indice >= len(self.dados):
            return None
        return self.dados.pop(indice)

    def recibir_daño(self, cantidad):
        self.vida -= cantidad
        if self.vida < 0:
            self.vida = 0

    def curarse(self, cantidad):
        self.vida += cantidad
        if self.vida > self.vida_maxima:
            self.vida = self.vida_maxima

    def es_muerto(self):
        return self.vida <= 0

    # Sistema básico de objetos (consumibles)
    def añadir_objeto(self, objeto):
        self.objetos.append(objeto)

    def usar_objeto(self, indice):
        if indice < 0 or indice >= len(self.objetos):
            return False
        obj = self.objetos.pop(indice)
        obj.aplicar(self)
        return True