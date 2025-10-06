import pygame
import sys
import defaults
from personaje import Personaje
from mundo import Mundo

pygame.init()

pantalla=pygame.display.set_mode((defaults.ANCHO, defaults.ALTO))
pygame.display.set_caption("Leñador")

def main():
    clock=pygame.time.Clock()
    mundo=Mundo(defaults.ANCHO, defaults.ALTO)
    personaje=Personaje(defaults.ANCHO // 2, defaults.ALTO // 2)
    
    respawn_timer=0
    esperando_respawn=False

    while True:
        dt = clock.tick(60)
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    personaje.interactuar(mundo)

        if (hasattr(mundo, 'pocion') and mundo.pocion and 
            mundo.pocion.activa and mundo.pocion.colision(personaje)):
            nuevo_personaje=mundo.pocion.aplicar_efecto(personaje)
            if nuevo_personaje is not None:
                personaje=nuevo_personaje
            mundo.pocion.activa=False
            esperando_respawn=True
            respawn_timer=defaults.APARICIONPOTI

        if esperando_respawn:
            respawn_timer-=dt
            if respawn_timer<=0:
                mundo.pocion=mundo.generar_pocion()
                esperando_respawn=False

        Teclas=pygame.key.get_pressed()
        dx, dy =0, 0
        
        if Teclas[pygame.K_LEFT]:
            dx=-5
        if Teclas[pygame.K_RIGHT]:
            dx=5
        if Teclas[pygame.K_UP]:
            dy=-5
        if Teclas[pygame.K_DOWN]:
            dy=5

        if dx !=0 or dy !=0:
            resultado_move=personaje.move(dx, dy, mundo)
            if resultado_move is not None:
                personaje=resultado_move
        
        if hasattr(personaje, 'actualizar_animacion'):
            personaje.actualizar_animacion(dt)

        pantalla.fill((0, 0, 0))
        mundo.draw(pantalla)
        personaje.draw(pantalla)
        mundo.draw_inventario(pantalla, personaje)

        pygame.display.flip()

if __name__=="__main__":
    main()