from fabricas.fabrica_abstracta import FabricaAbstracta
from interfaces.arma import IArma
from interfaces.armadura import IArmadura
from interfaces.cuerpo import ICuerpo
from interfaces.montura import IMontura

class Espada(IArma):
    def get_descripcion(self):
        return "Espada de acero"

class ArmaduraPlacas(IArmadura):
    def get_descripcion(self):
        return "Armadura de placas"

class CuerpoHumano(ICuerpo):
    def get_descripcion(self):
        return "Físico balanceado"

class Caballo(IMontura):
    def get_descripcion(self):
        return "Caballo de guerra"

class FabricaHumanos(FabricaAbstracta):
    def crear_arma(self):
        return Espada()
    def crear_armadura(self):
        return ArmaduraPlacas()
    def crear_cuerpo(self):
        return CuerpoHumano()
    def crear_montura(self):
        return Caballo()
