"""fabrica_objetos.py
Factory Method para crear instancias de objetos según su tipo.
"""

from objeto import (
    ObjetoAumentoAtaque,
    ObjetoAumentoDefensa,
    ObjetoBandita,
    ObjetoDadosPlata,
    ObjetoPiromancia,
    ObjetoPergaminoProteccion,
    ObjetoDadosOro,
    ObjetoDadoFantasma,
    ObjetoDefensaAbsoluta,
)


class FabricaObjetos:
    def crear_objeto(self, tipo: str):
        tipo = tipo.lower()
        if tipo == "aumento_ataque":
            return ObjetoAumentoAtaque()
        if tipo == "aumento_defensa":
            return ObjetoAumentoDefensa()
        if tipo == "bandita":
            return ObjetoBandita()
        if tipo == "dados_plata":
            return ObjetoDadosPlata()
        if tipo == "piromancia":
            return ObjetoPiromancia()
        if tipo == "pergamino_proteccion":
            return ObjetoPergaminoProteccion()
        if tipo == "dados_oro":
            return ObjetoDadosOro()
        if tipo == "dado_fantasma":
            return ObjetoDadoFantasma()
        if tipo == "defensa_absoluta":
            return ObjetoDefensaAbsoluta()
        return ObjetoBandita()
