from fabricas.fabrica_abstracta import FabricaAbstracta
from interfaces.arma import IArma
from interfaces.armadura import IArmadura
from interfaces.cuerpo import ICuerpo
from interfaces.montura import IMontura

class Arma(IArma):
    def get_descripcion(self):
        return "Martillo de batalla enano"

class Armadura(IArmadura):
    def get_descripcion(self):
        return "Armadura rúnica reforzada"

class Cuerpo(ICuerpo):
    def get_descripcion(self):
        return "Robusto y resistente"

class Montura(IMontura):
    def get_descripcion(self):
        return "Jabalí de guerra"

class FabricaEnanos(FabricaAbstracta):
    def crear_arma(self):
        return Arma()
    def crear_armadura(self):
        return Armadura()
    def crear_cuerpo(self):
        return Cuerpo()
    def crear_montura(self):
        return Montura()
