"""jugador.py
Modelo de Jugador: vida, dados, rerolls, escudos, DOT, objetos, etc.
"""

import random
from configuracion import DADOS_INICIALES, MAX_REROLLS_POR_TURNO, VIDA_INICIAL


class Dado:
    """Dado con valor y bandera de si es fantasma."""

    def __init__(self, valor: int, es_fantasma: bool = False):
        self.valor = valor
        self.es_fantasma = es_fantasma

    def copiar(self):
        return Dado(self.valor, self.es_fantasma)


class EfectoDOT:
    def __init__(self, daño_por_turno: int, turnos: int):
        self.daño_por_turno = daño_por_turno
        self.turnos_restantes = turnos


class Jugador:
    def __init__(self, nombre: str, vida_maxima: int = VIDA_INICIAL, cartas=None, inventario=None):
        self.nombre = nombre
        self.vida = vida_maxima
        self.vida_maxima = vida_maxima

        self.cartas = cartas or []
        self.inventario = inventario 

        self.dados: list[Dado] = []
        self.perder_dados_siguiente_turno = 0

        self.rerolls_realizados = 0
        self.puede_usar_reroll = True
        self.bloquear_reroll_proximo_turno = False

        self.objeto_usado_en_turno = False

        self.bono_ataque_turno = 0
        self.escudo_puntos = 0
        self.bloqueos_totales = 0
        self.efectos_dot: list[EfectoDOT] = []

    def iniciar_turno(self):
        if self.bloquear_reroll_proximo_turno:
            self.puede_usar_reroll = False
            self.bloquear_reroll_proximo_turno = False
        else:
            self.puede_usar_reroll = True

        self._aplicar_dot_inicio_turno()

        self.bono_ataque_turno = 0
        self.objeto_usado_en_turno = False
        self.escudo_puntos = 0

        for carta in self.cartas:
            carta.resetear_turno()

        cantidad = DADOS_INICIALES - self.perder_dados_siguiente_turno
        if cantidad < 1:
            cantidad = 1
        self.perder_dados_siguiente_turno = 0

        self.dados = [Dado(random.randint(1, 6)) for _ in range(cantidad)]
        self.rerolls_realizados = 0

    def finalizar_turno(self):
        if self.rerolls_realizados > 0:
            self.bloquear_reroll_proximo_turno = True

    def hacer_reroll(self):
        if not self.puede_usar_reroll:
            return False
        if self.rerolls_realizados >= MAX_REROLLS_POR_TURNO:
            return False
        if not self.dados:
            return False

        self.rerolls_realizados += 1
        nuevos_dados = []
        for _ in range(len(self.dados)):
            valor = random.randint(1, 6) + self.rerolls_realizados
            if valor > 8:
                valor = 8
            nuevos_dados.append(Dado(valor))
        self.dados = nuevos_dados

        self.perder_dados_siguiente_turno = min(self.rerolls_realizados, 2)
        return True

    def usar_dado(self, indice: int) -> Dado | None:
        if indice < 0 or indice >= len(self.dados):
            return None
        return self.dados.pop(indice)

    def agregar_dado_fantasma(self, valor: int):
        self.dados.append(Dado(valor, es_fantasma=True))

    def recibir_daño(self, cantidad: int):
        if cantidad <= 0:
            return
        if self.bloqueos_totales > 0:
            self.bloqueos_totales -= 1
            return

        if self.escudo_puntos > 0:
            absorbido = min(cantidad, self.escudo_puntos)
            self.escudo_puntos -= absorbido
            cantidad -= absorbido

        if cantidad <= 0:
            return

        self.vida -= cantidad
        if self.vida < 0:
            self.vida = 0

    def curarse(self, cantidad: int):
        if cantidad <= 0:
            return
        self.vida += cantidad
        if self.vida > self.vida_maxima:
            self.vida = self.vida_maxima

    def es_muerto(self) -> bool:
        return self.vida <= 0

    def agregar_escudo(self, puntos: int):
        self.escudo_puntos += max(0, puntos)

    def agregar_dot(self, daño_por_turno: int, turnos: int):
        if daño_por_turno <= 0 or turnos <= 0:
            return
        self.efectos_dot.append(EfectoDOT(daño_por_turno, turnos))

    def _aplicar_dot_inicio_turno(self):
        efectos_restantes = []
        for efecto in self.efectos_dot:
            self.recibir_daño(efecto.daño_por_turno)
            efecto.turnos_restantes -= 1
            if efecto.turnos_restantes > 0:
                efectos_restantes.append(efecto)
        self.efectos_dot = efectos_restantes