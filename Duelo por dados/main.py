"""main.py
Punto de entrada del juego. Maneja la ventana de pygame y los eventos de interacción.
"""
import pygame
from configuracion import ANCHO, ALTO, FPS, NOMBRE_JUEGO
from gestor_recursos import GestorRecursos
from jugador import Jugador
from fabrica_cartas import FabricaCartas
from turno import TurnoManager
from gestor_memento import GestorMemento

pygame.init()
pygame.display.set_caption(NOMBRE_JUEGO)
ventana = pygame.display.set_mode((ANCHO, ALTO))
reloj = pygame.time.Clock()

# Cargar recursos (opcional)
gestor_recursos = GestorRecursos.get_instancia()
# ejemplo: gestor_recursos.cargar_imagen('fondo', 'assets/fondo.png')

# Crear cartas y jugadores
fabrica = FabricaCartas()
cartas_base = [fabrica.crear_carta('ataque'), fabrica.crear_carta('cura'), fabrica.crear_carta('defensa')]

jugador1 = Jugador('Jugador 1', vida_maxima=20, cartas=[carta for carta in cartas_base])
jugador2 = Jugador('Jugador 2', vida_maxima=20, cartas=[carta for carta in cartas_base])

# Memento manager para rerolls
gestor_memento = GestorMemento()

# Turn manager con Chain of Responsibility
turno_manager = TurnoManager([jugador1, jugador2])

# Variables UI
fuente = pygame.font.SysFont(None, 24)
seleccion_dado = None  # índice del dado seleccionado
seleccion_carta = None
mensaje_info = ''

running = True
while running:
    dt = reloj.tick(FPS)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False
        elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            mx, my = evento.pos
            turno_actual = turno_manager.turno_actual
            # Botón reroll
            if 20 <= mx <= 140 and 430 <= my <= 470:
                # guardar estado antes de reroll
                gestor_memento.guardar(turno_actual)
                exito = turno_actual.hacer_reroll()
                if not exito:
                    mensaje_info = 'No puedes rerollear más (máx 2) o no hay dados.'
                else:
                    mensaje_info = f'Rerroll hecho (+{turno_actual.rerolls_realizados} a tiradas nuevas).'
            # Botón restaurar (undo reroll)
            if 160 <= mx <= 320 and 430 <= my <= 470:
                exito = gestor_memento.restaurar(turno_actual)
                mensaje_info = 'Tirada restaurada.' if exito else 'Nada que restaurar.'
            # Botón terminar turno
            if 360 <= mx <= 520 and 430 <= my <= 470:
                turno_manager.siguiente_fase()
                mensaje_info = f'Terminado turno de {turno_actual.nombre}.'
            # Click en dados
            for i in range(len(turno_actual.dados)):
                x = 20 + i * 60
                if x <= mx <= x + 50 and 50 <= my <= 100:
                    seleccion_dado = i
                    mensaje_info = f'Dado {i+1} seleccionado (valor {turno_actual.dados[i]}).'
            # Click en cartas
            for i in range(len(turno_actual.cartas)):
                cx = 20 + i * 200
                if cx <= mx <= cx + 180 and 150 <= my <= 260:
                    seleccion_carta = i
                    # si hay dado seleccionado, aplicarlo
                    if seleccion_dado is not None:
                        potencia = turno_actual.usar_dado(seleccion_dado)
                        if potencia is not None:
                            carta = turno_actual.cartas[seleccion_carta]
                            # aplicar carta: ataque usa objetivo, cura usa actor, defensa actor
                            objetivo = turno_manager.obtener_oponente()
                            carta.estrategia.aplicar(turno_actual, objetivo, potencia)
                            mensaje_info = f'{turno_actual.nombre} usó {carta.nombre} con potencia {potencia}.'
                            # comprobar muerte
                            if objetivo.es_muerto():
                                mensaje_info = f'{turno_actual.nombre} ha ganado!'
                            seleccion_dado = None
                            seleccion_carta = None

    # Actualizar lógica
    ventana.fill((25, 25, 30))

    # Dibujar UI: jugador actual
    jugador_act = turno_manager.turno_actual
    texto_turno = fuente.render(f'Turno de: {jugador_act.nombre}', True, (255, 255, 255))
    ventana.blit(texto_turno, (20, 10))

    # Dados
    for i, d in enumerate(jugador_act.dados):
        x = 20 + i * 60
        color = (220, 220, 220)
        if seleccion_dado == i:
            color = (255, 215, 0)
        pygame.draw.rect(ventana, color, (x, 50, 50, 50))
        txt = fuente.render(str(d), True, (0, 0, 0))
        ventana.blit(txt, (x + 18, 65))

    # Cartas
    for i, carta in enumerate(jugador_act.cartas):
        cx = 20 + i * 200
        color = (100, 100, 120)
        if seleccion_carta == i:
            color = (80, 140, 200)
        pygame.draw.rect(ventana, color, (cx, 150, 180, 110))
        txt = fuente.render(carta.nombre.capitalize(), True, (255, 255, 255))
        ventana.blit(txt, (cx + 10, 160))
        desc = fuente.render(carta.estrategia.descripcion_corta(), True, (220, 220, 220))
        ventana.blit(desc, (cx + 10, 190))

    # Botones
    pygame.draw.rect(ventana, (80, 150, 80), (20, 430, 120, 40))
    ventana.blit(fuente.render('Reroll', True, (255, 255, 255)), (30, 440))
    pygame.draw.rect(ventana, (80, 120, 200), (160, 430, 160, 40))
    ventana.blit(fuente.render('Restaurar', True, (255, 255, 255)), (170, 440))
    pygame.draw.rect(ventana, (150, 50, 50), (360, 430, 160, 40))
    ventana.blit(fuente.render('Terminar Turno', True, (255, 255, 255)), (370, 440))

    # Mostrar vidas
    v1 = fuente.render(f'{turno_manager.jugadores[0].nombre}: {turno_manager.jugadores[0].vida}', True, (255, 255, 255))
    v2 = fuente.render(f'{turno_manager.jugadores[1].nombre}: {turno_manager.jugadores[1].vida}', True, (255, 255, 255))
    ventana.blit(v1, (480, 50))
    ventana.blit(v2, (480, 80))

    # Mensaje informativo
    ventana.blit(fuente.render(mensaje_info, True, (255, 255, 255)), (20, 300))

    pygame.display.flip()

    # comprobar fin de partida
    if turno_manager.jugadores[0].es_muerto() or turno_manager.jugadores[1].es_muerto():
        # Mostrar mensaje final y esperar 2 segundos
        ganador = turno_manager.jugadores[0] if turno_manager.jugadores[1].es_muerto() else turno_manager.jugadores[1]
        print(f'Fin de partida. ganador: {ganador.nombre}')
        pygame.time.delay(2000)
        running = False

pygame.quit()