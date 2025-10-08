import pygame

class ControlAdapter:
    """
    Clase base (interfaz) para el patrón Adapter.

    Define el método obtener_movimiento(), que debe ser implementado por
    las clases adaptadoras concretas (TecladoAdapter y MouseAdapter).
    """

    def obtener_movimiento(self, personaje):
        """
        Retorna el movimiento (dx, dy) que debe realizar el personaje.

        Este método debe ser implementado por las subclases.
        """
        raise NotImplementedError


class TecladoAdapter(ControlAdapter):
    """
    Adaptador concreto que traduce la entrada del teclado en movimiento.
    """

    def obtener_movimiento(self, personaje):
        """
        Retorna (dx, dy) según las teclas presionadas (flechas direccionales).
        """
        teclas = pygame.key.get_pressed()
        dx, dy = 0, 0
        velocidad = 5

        if teclas[pygame.K_LEFT]:
            dx = -velocidad
        if teclas[pygame.K_RIGHT]:
            dx = velocidad
        if teclas[pygame.K_UP]:
            dy = -velocidad
        if teclas[pygame.K_DOWN]:
            dy = velocidad

        return dx, dy


class MouseAdapter(ControlAdapter):
    """
    Adaptador concreto que traduce la posición del mouse en movimiento.

    El personaje se desplazará gradualmente hacia la posición del cursor.
    """

    def obtener_movimiento(self, personaje):
        """
        Calcula el desplazamiento (dx, dy) del personaje hacia el cursor.

        Retorna un movimiento suave en dirección al mouse.
        """
        mouse_x, mouse_y = pygame.mouse.get_pos()
        dx, dy = 0, 0
        velocidad = 5

        # Movimiento gradual hacia el cursor
        if abs(personaje.x - mouse_x) > 5:
            dx = velocidad if mouse_x > personaje.x else -velocidad
        if abs(personaje.y - mouse_y) > 5:
            dy = velocidad if mouse_y > personaje.y else -velocidad

        return dx, dy
