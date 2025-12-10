"""gestor_recursos.py
Singleton sencillo para manejar imágenes (cartas, dados, fondos).
"""
import pygame
import os
import sys

class GestorRecursos:
    _instancia = None

    def __init__(self):
        if GestorRecursos._instancia is not None:
            raise Exception("Usa GestorRecursos.get_instancia()")
        self.imagenes = {}

    @classmethod
    def get_instancia(cls):
        if cls._instancia is None:
            cls._instancia = GestorRecursos()
        return cls._instancia

    def cargar_imagen(self, llave: str, ruta: str):
        if llave not in self.imagenes:
            if not os.path.exists(ruta):
                raise FileNotFoundError(ruta)
            self.imagenes[llave] = pygame.image.load(ruta).convert_alpha()
        return self.imagenes[llave]

    def obtener_imagen(self, llave: str):
        return self.imagenes.get(llave)
    
    def ruta_absoluta(relativa):
        if hasattr(sys, "_MEIPASS"):
            return os.path.join(sys._MEIPASS, relativa)
        return os.path.join(os.getcwd(), relativa)
