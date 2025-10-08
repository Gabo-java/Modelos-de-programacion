import pygame
import sys
import defaults
from personaje import Personaje
from mundo import Mundo
from control_adapter import TecladoAdapter, MouseAdapter

pygame.init()

# Configuración inicial de la ventana
pantalla = pygame.display.set_mode((defaults.ANCHO, defaults.ALTO))
pygame.display.set_caption("Leñador")

def main():
    """
    Función principal del juego.

    Maneja el ciclo de ejecución de Pygame, el control del personaje
    mediante el patrón Adapter y la lógica del mundo.
    """
    clock = pygame.time.Clock()
    mundo = Mundo(defaults.ANCHO, defaults.ALTO)
    personaje = Personaje(defaults.ANCHO // 2, defaults.ALTO // 2)

    # Inicializa el control usando el adaptador de teclado por defecto
    control_actual = TecladoAdapter()
    modo_control = "teclado"

    # Variables para control del respawn de pociones
    respawn_timer = 0
    esperando_respawn = False

    while True:
        dt = clock.tick(60)  # Controla FPS

        # === Manejo de eventos ===
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Interacción y cambio de modo de control
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    personaje.interactuar(mundo)
                if event.key == pygame.K_c:
                    # Alterna entre control por teclado y mouse
                    if modo_control == "teclado":
                        control_actual = MouseAdapter()
                        modo_control = "mouse"
                    else:
                        control_actual = TecladoAdapter()
                        modo_control = "teclado"

        # === Lógica de pociones ===
        if (hasattr(mundo, 'pocion') and mundo.pocion and 
            mundo.pocion.activa and mundo.pocion.colision(personaje)):
            nuevo_personaje = mundo.pocion.aplicar_efecto(personaje)
            if nuevo_personaje is not None:
                personaje = nuevo_personaje
            mundo.pocion.activa = False
            esperando_respawn = True
            respawn_timer = defaults.APARICIONPOTI

        if esperando_respawn:
            respawn_timer -= dt
            if respawn_timer <= 0:
                mundo.pocion = mundo.generar_pocion()
                esperando_respawn = False

        # === Movimiento del personaje (usando el Adapter actual) ===
        dx, dy = control_actual.obtener_movimiento(personaje)

        if dx != 0 or dy != 0:
            resultado_move = personaje.move(dx, dy, mundo)
            if resultado_move is not None:
                personaje = resultado_move

        # === Actualización de animación ===
        if hasattr(personaje, 'actualizar_animacion'):
            personaje.actualizar_animacion(dt)

        # === Renderizado de la escena ===
        pantalla.fill((0, 0, 0))
        mundo.draw(pantalla)
        personaje.draw(pantalla)
        mundo.draw_inventario(pantalla, personaje)

        pygame.display.flip()  # Actualiza la pantalla

if __name__ == "__main__":
    main()
