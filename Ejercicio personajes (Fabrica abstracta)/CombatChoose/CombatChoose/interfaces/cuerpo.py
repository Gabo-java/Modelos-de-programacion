from abc import ABC, abstractmethod

class ICuerpo(ABC):
    @abstractmethod
    def get_descripcion(self):
        pass