from abc import ABC, abstractmethod

class IMontura(ABC):
    @abstractmethod
    def get_descripcion(self):
        pass