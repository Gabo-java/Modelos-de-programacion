from abc import ABC, abstractmethod

class IArma(ABC):
    @abstractmethod
    def get_descripcion(self):
        pass