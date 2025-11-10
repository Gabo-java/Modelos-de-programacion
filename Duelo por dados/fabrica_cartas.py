"""fabrica_cartas.py
Factory Method simple para crear cartas con su estrategia.
"""
from carta import Carta, AtaqueEstrategia, CuraEstrategia, DefensaEstrategia

class FabricaCartas:
    def crear_carta(self, tipo):
        tipo = tipo.lower()
        if tipo == 'ataque':
            return Carta('ataque', AtaqueEstrategia())
        if tipo == 'cura':
            return Carta('cura', CuraEstrategia())
        if tipo == 'defensa':
            return Carta('defensa', DefensaEstrategia())
        # por defecto
        return Carta('genérica', AtaqueEstrategia())
