import pygame
import random
import os
import defaults

class Arbol:
    def __init__(self, x, y):
        self.x=x
        self.y=y
        self.madera=3

        arbol_path=os.path.join('assets','imagenes','objetos','Arbol.png')
        self.imagen_arbol=pygame.image.load(arbol_path).convert_alpha()
        self.imagen_arbol=pygame.transform.scale(self.imagen_arbol, size=(defaults.ARBOL, defaults.ARBOL))
        self.size=self.imagen_arbol.get_width()


    def draw(self, pantalla):
       pantalla.blit(self.imagen_arbol, (self.x, self.y))

    def talar (self):
        if self.madera>0:
            self.madera-=1
            return True
        return False