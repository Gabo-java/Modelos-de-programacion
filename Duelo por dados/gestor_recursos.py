"""gestor_recursos.py
Gestor de recursos (Singleton). Maneja la carga de imágenes y sonidos.
"""
import pygame

class GestorRecursos:
    _instancia = None

    def __init__(self):
        if GestorRecursos._instancia is not None:
            raise Exception('Usar get_instancia() para obtener el Gestor')
        self.imagenes = {}
        self.sonidos = {}

    @classmethod
    def get_instancia(cls):
        if cls._instancia is None:
            cls._instancia = GestorRecursos()
        return cls._instancia

    def cargar_imagen(self, llave, ruta):
        imagen = pygame.image.load(ruta).convert_alpha()
        self.imagenes[llave] = imagen
        return imagen

    def obtener_imagen(self, llave):
        return self.imagenes.get(llave)

    def cargar_sonido(self, llave, ruta):
        sonido = pygame.mixer.Sound(ruta)
        self.sonidos[llave] = sonido
        return sonido

    def obtener_sonido(self, llave):
        return self.sonidos.get(llave)