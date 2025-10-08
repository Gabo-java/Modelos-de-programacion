import pygame
import random
import defaults
from decoradores import Aura, Velocidad, Fuego  

class Potis:
    def __init__(self, x, y, tipo):
        self.x=x
        self.y=y
        self.tipo=tipo  
        self.tamaño=defaults.TAMAÑOPOTI
        self.color=self.obtener_color()
        self.texto=self.obtener_texto()
        self.activa=True
    
    def obtener_color(self):
        if self.tipo=='aura':
            return defaults.POCIONAU
        elif self.tipo=='velocidad':
            return defaults.POCIONVEL
        else:  
            return defaults.POCIONFUE
         
    def obtener_texto(self):
        if self.tipo=='aura':
            return "AURA"
        elif self.tipo =='velocidad':
            return "VEL"
        else:  # fuego
            return "FGO"
    
    def draw(self, pantalla):
        if not self.activa:
            return
            
        pygame.draw.circle(pantalla, self.color, (self.x + self.tamaño//2, self.y + self.tamaño//2), self.tamaño//2)
        pygame.draw.circle(pantalla, (255, 255, 255), (self.x + self.tamaño//2, self.y + self.tamaño//2), self.tamaño//2, 2)
        
        font=pygame.font.SysFont("comic Sans MS", 10, bold=True)
        texto=font.render(self.texto, True, (255, 255, 255))
        texto_rect=texto.get_rect(center=(self.x + self.tamaño//2, self.y + self.tamaño//2))
        pantalla.blit(texto, texto_rect)
    
    def colision(self, personaje):
        if not self.activa:
            return False
            
        return (personaje.x<self.x+self.tamaño and
                personaje.x+personaje.tamaño>self.x and
                personaje.y<self.y+self.tamaño and
                personaje.y+personaje.tamaño>self.y)
    
    def aplicar_efecto(self, personaje):
        if not self.activa:
            return personaje
    
        if self.tipo=='aura':
            return Aura(personaje) 
        elif self.tipo=='velocidad':
            return Velocidad(personaje)  
        else:  
            return Fuego(personaje)