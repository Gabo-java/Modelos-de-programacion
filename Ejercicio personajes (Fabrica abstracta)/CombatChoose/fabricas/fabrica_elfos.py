from fabricas.fabrica_abstracta import FabricaAbstracta
from interfaces.arma import IArma
from interfaces.armadura import IArmadura
from interfaces.cuerpo import ICuerpo
from interfaces.montura import IMontura

class Arco(IArma):
    def get_descripcion(self):
        return "Arco largo élfico"

class ArmaduraLigera(IArmadura):
    def get_descripcion(self):
        return "Armaduras de cuero ligero"

class CuerpoElfo(ICuerpo):
    def get_descripcion(self):
        return "Ágil y elegante"

class Ciervo(IMontura):
    def get_descripcion(self):
        return "Ciervo místico"

class FabricaElfos(FabricaAbstracta):
    def crear_arma(self):
        return Arco()
    def crear_armadura(self):
        return ArmaduraLigera()
    def crear_cuerpo(self):
        return CuerpoElfo()
    def crear_montura(self):
        return Ciervo()

