"""configuracion.py
Configuración general del juego y estilos TCG.
"""

# Tamaño de la ventana (formato 16:9 estilo juego de cartas)
ANCHO_VENTANA = 1320
ALTO_VENTANA = 760
FPS = 60

NOMBRE_JUEGO = "Duelos por Dados TCG"

# Tamaño de las cartas (TCG style)
CARTA_ANCHO = 220
CARTA_ALTO = 320

# Tamaño de los dados
DADO_TAM = 96

# Valores de juego
DADOS_INICIALES = 3
VIDA_INICIAL = 20
MAX_REROLLS_POR_TURNO = 2

# Estilos de cartas (colores de fallback si no se usan imágenes)
ESTILOS_CARTAS = {
    "ataque": {
        "color_fondo": (110, 40, 40),
        "color_borde": (190, 90, 90),
    },
    "cura": {
        "color_fondo": (40, 110, 60),
        "color_borde": (90, 190, 120),
    },
    "defensa": {
        "color_fondo": (40, 60, 130),
        "color_borde": (90, 120, 200),
    },
    "objetos": {
        "color_fondo": (130, 100, 40),
        "color_borde": (210, 180, 110),
    },
}
