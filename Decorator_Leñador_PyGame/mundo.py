import pygame
import defaults
import random
import os
from visuales import Arbol
from potis import Potis

class Mundo:
    def __init__(self, ANCHO, ALTO):
        self.ANCHO=ANCHO
        self.ALTO=ALTO
        self.arboles=self.generador_arboles(15) 
        self.pocion=self.generar_pocion()  

        pasto_path=os.path.join('assets','imagenes','objetos','Pasto.png')
        self.imagen_pasto=pygame.image.load(pasto_path).convert_alpha()
        self.imagen_pasto=pygame.transform.scale(self.imagen_pasto, size=(defaults.PASTO, defaults.PASTO))

    def generador_arboles(self, cantidad):
        arboles=[]
        for _ in range(cantidad):
            x=random.randint(0, self.ANCHO-50)  
            y=random.randint(0, self.ALTO-50) 
            arbol=Arbol(x, y)
            arboles.append(arbol)
        return arboles

    def generar_pocion(self):
        x=random.randint(0, self.ANCHO-defaults.TAMAÑOPOTI)
        y=random.randint(0, self.ALTO-defaults.TAMAÑOPOTI)
        
        tipos=['aura', 'velocidad', 'fuego']
        tipo=random.choice(tipos)
        
        return Potis(x, y, tipo)

    def draw(self, pantalla):
        for y in range(0, self.ALTO, defaults.PASTO):
            for x in range(0, self.ANCHO, defaults.PASTO):
                pantalla.blit(self.imagen_pasto, (x, y))
        
        for arbol in self.arboles:
            arbol.draw(pantalla)

        if self.pocion.activa:
            self.pocion.draw(pantalla)

    def draw_inventario(self, pantalla, personaje):
        Texto=pygame.font.SysFont("Comic Sans MS", 30)
        madera=Texto.render(f"Madera: {personaje.inventario['madera']}", True, defaults.BLANCO)
        pantalla.blit(madera, (10, 10))

        pociones_aura=getattr(personaje, 'pociones_aura', 0)
        pociones_velocidad=getattr(personaje, 'pociones_velocidad', 0)
        pociones_fuego=getattr(personaje, 'pociones_fuego', 0)
        
        aura_texto=Texto.render(f"Aura: {pociones_aura}", True, defaults.POCIONAU)
        velocidad_texto=Texto.render(f"Velocidad: {pociones_velocidad}", True, defaults.POCIONVEL)
        fuego_texto=Texto.render(f"Fuego: {pociones_fuego}", True, defaults.POCIONFUE)
        
        pantalla.blit(aura_texto, (10, 50))
        pantalla.blit(velocidad_texto, (10, 90))
        pantalla.blit(fuego_texto, (10, 130))