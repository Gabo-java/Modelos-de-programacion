import pygame, sys
from default import *
from Controlador_juego import ControladorJuego
from command import ComandoActivarPalanca
from mundo import palancas

pygame.init()
pantalla=pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Ruleta Bombástica")
reloj=pygame.time.Clock()

def main():
    juego=ControladorJuego(pantalla)
    handler_actual=juego.cadena_jugadores[0].manejar(juego)

    while True:
        for evento in pygame.event.get():
            if evento.type==pygame.QUIT:
                pygame.quit()
                sys.exit()

            #Pequeño tecla para ver la posicion actual de la palanca que activa la bomba
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_d:
                juego.debug_activo ^= True

            if evento.type==pygame.MOUSEBUTTONDOWN and evento.button==1:
                if juego.turno_actual:
                    pos=pygame.mouse.get_pos()
                    for i, palanca in enumerate(palancas):
                        if palanca.collidepoint(pos):
                            comando=ComandoActivarPalanca(juego.turno_actual, i, juego)
                            accion_valida=comando.ejecutar()

                            if accion_valida:
                                ganador=juego.hay_ganador()
                                if ganador:
                                    juego.mostrar_mensaje(f"{ganador['nombre']} gana el juego")
                                    juego.actualizar_pantalla()
                                    pygame.time.delay(DELAY_FIN)
                                    pygame.quit()
                                    sys.exit()

                                handler_actual = juego.siguiente_turno(handler_actual)
                            break

        juego.actualizar_pantalla()
        reloj.tick(FPS)

if __name__ == "__main__":
    main()
