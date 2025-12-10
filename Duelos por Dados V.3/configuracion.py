"""configuracion.py
Constantes y estilos de UI del juego.
"""

ANCHO = 900
ALTO = 550
FPS = 30
NOMBRE_JUEGO = "Duelos por Dados 2.0"

DADOS_INICIALES = 3
VIDA_INICIAL = 20
MAX_REROLLS_POR_TURNO = 2

# Estilos de cartas (para que puedas cambiar “skins” sin tocar la lógica)
ESTILOS_CARTAS = {
    "ataque": {
        "color_fondo": (170, 60, 60),
        "color_borde": (220, 120, 120),
    },
    "cura": {
        "color_fondo": (60, 140, 60),
        "color_borde": (120, 200, 120),
    },
    "defensa": {
        "color_fondo": (60, 90, 160),
        "color_borde": (130, 150, 220),
    },
    "objetos": {
        "color_fondo": (160, 130, 60),
        "color_borde": (220, 190, 120),
    },
}
