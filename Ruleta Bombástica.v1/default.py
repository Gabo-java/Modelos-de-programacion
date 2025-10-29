import pygame

#Valores predeterminados del juego
ANCHO, ALTO=800, 600
FPS=60

#Colores usados en el juego
BLANCO=(255, 255, 255)
NEGRO=(0, 0, 0)
ROJO=(255, 0, 0)
AZUL=(0, 0, 255)
VERDE=(0, 255, 0)
AMARILLO=(255, 255, 0)
GRIS=(120, 120, 120)
GRIS_OSCURO=(60, 60, 60)

#Representacion de los jugadores
RADIO_JUGADOR=30
Y_JUGADOR=500

#Representacion de las palancas
TAMANO_PALANCA=50
X_INICIAL=150
ESPACIO_PALANCA=120
Y_PALANCA=300

#Tiempos de espera
DELAY_MENSAJE=1500
DELAY_EXPLOSION=2000
DELAY_ELIMINADO=1500
DELAY_FIN=4000

#Fuente de texto
pygame.font.init()
FUENTE=pygame.font.SysFont("Comic Sans MS", 28)