"""objeto.py
Objetos de un solo uso con diferentes calidades.
"""

class ObjetoBase:
    def __init__(self, nombre: str, calidad: str):
        self.nombre = nombre
        self.calidad = calidad  # "baja", "media", "alta"

    def aplicar(self, jugador, enemigo, contexto: dict):
        raise NotImplementedError

    def resetear(self):
        """Si el objeto tuviera estado interno, aquí se limpiaría antes de volver al pool."""
        pass


# --------- CALIDAD BAJA ----------

class ObjetoAumentoAtaque(ObjetoBase):
    def __init__(self):
        super().__init__("Aumento de ataque", "baja")

    def aplicar(self, jugador, enemigo, contexto: dict):
        jugador.bono_ataque_turno += 2


class ObjetoAumentoDefensa(ObjetoBase):
    def __init__(self):
        super().__init__("Aumento de defensa", "baja")

    def aplicar(self, jugador, enemigo, contexto: dict):
        jugador.agregar_escudo(2)


class ObjetoBandita(ObjetoBase):
    def __init__(self):
        super().__init__("Bandita", "baja")

    def aplicar(self, jugador, enemigo, contexto: dict):
        jugador.curarse(2)


# --------- CALIDAD MEDIA ----------

class ObjetoDadosPlata(ObjetoBase):
    def __init__(self):
        super().__init__("Dados de plata", "media")

    def aplicar(self, jugador, enemigo, contexto: dict):
        for dado in jugador.dados:
            dado.valor += 2


class ObjetoPiromancia(ObjetoBase):
    def __init__(self):
        super().__init__("Piromancia", "media")

    def aplicar(self, jugador, enemigo, contexto: dict):
        enemigo.recibir_daño(2)
        enemigo.agregar_dot(daño_por_turno=2, turnos=3)


class ObjetoPergaminoProteccion(ObjetoBase):
    def __init__(self):
        super().__init__("Pergamino de protección", "media")

    def aplicar(self, jugador, enemigo, contexto: dict):
        jugador.curarse(4)
        jugador.agregar_escudo(2)


# --------- CALIDAD ALTA ----------

class ObjetoDadosOro(ObjetoBase):
    def __init__(self):
        super().__init__("Dados de oro", "alta")

    def aplicar(self, jugador, enemigo, contexto: dict):
        for dado in jugador.dados:
            dado.valor += 3


class ObjetoDadoFantasma(ObjetoBase):
    def __init__(self):
        super().__init__("Dado fantasma", "alta")

    def aplicar(self, jugador, enemigo, contexto: dict):
        import random
        valor = random.randint(4, 8)
        jugador.agregar_dado_fantasma(valor)


class ObjetoDefensaAbsoluta(ObjetoBase):
    def __init__(self):
        super().__init__("Defensa absoluta", "alta")

    def aplicar(self, jugador, enemigo, contexto: dict):
        jugador.bloqueos_totales += 2
