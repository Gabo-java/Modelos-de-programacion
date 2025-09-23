from abc import ABC, abstractmethod

class IArmadura(ABC):
    @abstractmethod
    def get_descripcion(self):
        pass