"""gestor_recursos.py
Singleton para manejar imágenes y sonidos (opcional).
"""
import pygame


class GestorRecursos:
    _instancia = None

    def __init__(self):
        if GestorRecursos._instancia is not None:
            raise Exception("Usa GestorRecursos.get_instancia()")
        self.imagenes = {}
        self.sonidos = {}

    @classmethod
    def get_instancia(cls):
        if cls._instancia is None:
            cls._instancia = GestorRecursos()
        return cls._instancia

    def cargar_imagen(self, llave: str, ruta: str):
        if llave not in self.imagenes:
            self.imagenes[llave] = pygame.image.load(ruta).convert_alpha()
        return self.imagenes[llave]

    def obtener_imagen(self, llave: str):
        return self.imagenes.get(llave)

    def cargar_sonido(self, llave: str, ruta: str):
        if llave not in self.sonidos:
            self.sonidos[llave] = pygame.mixer.Sound(ruta)
        return self.sonidos[llave]

    def obtener_sonido(self, llave: str):
        return self.sonidos.get(llave)
