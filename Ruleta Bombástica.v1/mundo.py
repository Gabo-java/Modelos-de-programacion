import pygame
import random
from default import *

#Posicionamiento de los jugadores
jugadores = [
    {"nombre":"J1", "color":ROJO, "pos":(150, Y_JUGADOR), "vivo":True},
    {"nombre":"J2", "color":AZUL, "pos":(300, Y_JUGADOR), "vivo":True},
    {"nombre":"J3", "color":VERDE, "pos":(450, Y_JUGADOR), "vivo":True},
    {"nombre":"J4", "color":AMARILLO, "pos":(600, Y_JUGADOR), "vivo":True},
]

#Posicionamiento de las palancas 
colores_palancas=[ROJO, AZUL, VERDE, BLANCO, NEGRO]
palancas=[
    pygame.Rect(X_INICIAL+i*ESPACIO_PALANCA,Y_PALANCA,TAMANO_PALANCA,TAMANO_PALANCA)
    for i in range(len(colores_palancas))
]

#Dibujo de la bomba
def dibujar_bomba(pantalla):
    pygame.draw.circle(pantalla,NEGRO, (400, 150), 40)
    pygame.draw.rect(pantalla,GRIS, (380, 90, 40, 20))
    pygame.draw.rect(pantalla,NEGRO, (390, 70, 20, 20))
    pygame.draw.line(pantalla,(255, 165, 0), (400, 60), (400, 50), 3)
