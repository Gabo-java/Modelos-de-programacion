from abc import ABC, abstractmethod

class FabricaAbstracta(ABC):
    @abstractmethod
    def crear_arma(self):
        pass

    @abstractmethod
    def crear_armadura(self):
        pass

    @abstractmethod
    def crear_cuerpo(self):
        pass

    @abstractmethod
    def crear_montura(self):
        pass
