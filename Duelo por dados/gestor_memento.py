"""gestor_memento.py
Memento simple para almacenar el estado de los dados antes de un reroll.
"""
class Memento:
    def __init__(self, dados, rerolls_hechos, perder_dados_siguiente_turno):
        self.dados = list(dados)
        self.rerolls_hechos = rerolls_hechos
        self.perder_dados_siguiente_turno = perder_dados_siguiente_turno

class GestorMemento:
    def __init__(self):
        # almacena mementos por jugador (nombre -> pila)
        self._pila_por_jugador = {}

    def guardar(self, jugador):
        pila = self._pila_por_jugador.setdefault(jugador.nombre, [])
        pila.append(Memento(jugador.dados, jugador.rerolls_realizados, jugador.perder_dados_siguiente_turno))

    def restaurar(self, jugador):
        pila = self._pila_por_jugador.get(jugador.nombre, [])
        if pila:
            m = pila.pop()
            jugador.dados = list(m.dados)
            jugador.rerolls_realizados = m.rerolls_hechos
            jugador.perder_dados_siguiente_turno = m.perder_dados_siguiente_turno
            return True
        return False