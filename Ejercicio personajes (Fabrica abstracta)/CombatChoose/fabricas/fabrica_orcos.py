from fabricas.fabrica_abstracta import FabricaAbstracta
from interfaces.arma import IArma
from interfaces.armadura import IArmadura
from interfaces.cuerpo import ICuerpo
from interfaces.montura import IMontura

class Hacha(IArma):
    def get_descripcion(self):
        return "Hacha de guerra brutal"

class ArmaduraPesada(IArmadura):
    def get_descripcion(self):
        return "Armadura de hierro pesado"

class CuerpoOrco(ICuerpo):
    def get_descripcion(self):
        return "Musculoso y feroz"

class Lobo(IMontura):
    def get_descripcion(self):
        return "Lobo gigante"

class FabricaOrcos(FabricaAbstracta):
    def crear_arma(self):
        return Hacha()
    def crear_armadura(self):
        return ArmaduraPesada()
    def crear_cuerpo(self):
        return CuerpoOrco()
    def crear_montura(self):
        return Lobo()
