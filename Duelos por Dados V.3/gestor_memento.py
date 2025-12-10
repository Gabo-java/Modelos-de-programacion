"""gestor_memento.py
Implementación de Memento para guardar tiradas antes de reroll.
"""

from jugador import Dado


class MementoTirada:
    def __init__(self, dados, rerolls_realizados, perder_dados_siguiente_turno):
        self.dados = [d.copiar() for d in dados]
        self.rerolls_realizados = rerolls_realizados
        self.perder_dados_siguiente_turno = perder_dados_siguiente_turno


class GestorMemento:
    """Gestiona pilas de mementos por jugador (nombre)."""

    def __init__(self):
        self._pila_por_jugador = {}

    def guardar(self, jugador):
        pila = self._pila_por_jugador.setdefault(jugador.nombre, [])
        memento = MementoTirada(
            jugador.dados,
            jugador.rerolls_realizados,
            jugador.perder_dados_siguiente_turno,
        )
        pila.append(memento)

    def restaurar(self, jugador):
        pila = self._pila_por_jugador.get(jugador.nombre, [])
        if not pila:
            return False
        memento = pila.pop()
        jugador.dados = [d.copiar() for d in memento.dados]
        jugador.rerolls_realizados = memento.rerolls_realizados
        jugador.perder_dados_siguiente_turno = memento.perder_dados_siguiente_turno
        return True
