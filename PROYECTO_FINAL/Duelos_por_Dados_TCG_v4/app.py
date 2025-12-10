"""main.py
Duelos por Dados TCG - Menú con dos modos: clásico y avanzado.
"""
import pygame

from configuracion import (
    ANCHO_VENTANA,
    ALTO_VENTANA,
    FPS,
    NOMBRE_JUEGO,
    CARTA_ANCHO,
    CARTA_ALTO,
    DADO_TAM,
)
from gestor_recursos import GestorRecursos
from gestor_memento import GestorMemento
from carta import (
    Carta,
    EstrategiaAtaque,
    EstrategiaCura,
    EstrategiaDefensa,
    EstrategiaObjetos,
)
from jugador import Jugador
from fabrica_objetos import FabricaObjetos
from object_pool import ObjectPoolObjetos
from turno import TurnoManager

ESTADO_MENU = "menu"
ESTADO_CLASICO = "clasico"
ESTADO_AVANZADO = "avanzado"

def crear_cartas_clasicas():
    return [
        Carta("Ataque", "ataque", EstrategiaAtaque()),
        Carta("Cura", "cura", EstrategiaCura()),
        Carta("Defensa", "defensa", EstrategiaDefensa()),
    ]

def crear_cartas_avanzadas():
    return [
        Carta("Ataque", "ataque", EstrategiaAtaque()),
        Carta("Cura", "cura", EstrategiaCura()),
        Carta("Defensa", "defensa", EstrategiaDefensa()),
        Carta("Objetos", "objetos", EstrategiaObjetos()),
    ]

def render_texto(superficie, texto, x, y, fuente, color=(255, 255, 255)):
    imagen = fuente.render(texto, True, color)
    superficie.blit(imagen, (x, y))

def dibujar_dado(ventana, gestor, dado, x, y):
    llave = f"dado_{dado.valor}"
    img = gestor.obtener_imagen(llave)
    if img is not None:
        img_scaled = pygame.transform.smoothscale(img, (DADO_TAM, DADO_TAM))
        ventana.blit(img_scaled, (x, y))
    else:
        color = (230, 230, 230)
        pygame.draw.rect(ventana, color, (x, y, DADO_TAM, DADO_TAM), border_radius=16)
        pygame.draw.rect(ventana, (40, 40, 40), (x, y, DADO_TAM, DADO_TAM), 3, border_radius=16)
        fuente_temp = pygame.font.SysFont(None, 32)
        txt = str(dado.valor)
        if dado.es_fantasma:
            txt += "F"
        render_texto(ventana, txt, x + DADO_TAM // 2 - 10, y + DADO_TAM // 2 - 10, fuente_temp, (0, 0, 0))

def dibujar_carta(ventana, gestor, carta, x, y, fuente):
    llave_img = f"carta_{carta.tipo}"
    img = gestor.obtener_imagen(llave_img)
    rect = pygame.Rect(x, y, CARTA_ANCHO, CARTA_ALTO)
    if img is not None:
        img_scaled = pygame.transform.smoothscale(img, (CARTA_ANCHO, CARTA_ALTO))
        ventana.blit(img_scaled, rect.topleft)
    else:
        estilos = carta.estilos()
        color_base = estilos["color_fondo"]
        color_borde = estilos["color_borde"]
        fondo = color_base
        pygame.draw.rect(ventana, fondo, rect, border_radius=16)
        pygame.draw.rect(ventana, color_borde, rect, 4, border_radius=16)

    if carta.usada_en_turno:
        overlay = pygame.Surface((CARTA_ANCHO, CARTA_ALTO), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 120))
        ventana.blit(overlay, rect.topleft)

    render_texto(ventana, "", x + 12, y + 12, fuente, (255, 255, 255))

def mostrar_menu(ventana, gestor):
    ventana.fill((10, 10, 15))
    fondo = gestor.obtener_imagen("fondo_menu")
    if fondo is not None:
        ventana.blit(pygame.transform.smoothscale(fondo, (ANCHO_VENTANA, ALTO_VENTANA)), (0, 0))

    fuente_titulo = pygame.font.Font(None, 72)
    fuente_botones = pygame.font.Font(None, 42)

    titulo = fuente_titulo.render("Duelos por Dados", True, (255, 255, 255))
    ventana.blit(titulo, (ANCHO_VENTANA // 2 - titulo.get_width() // 2, 80))

    boton_clasico = pygame.Rect(ANCHO_VENTANA // 2 - 220, 260, 440, 80)
    boton_avanzado = pygame.Rect(ANCHO_VENTANA // 2 - 220, 370, 440, 80)

    pygame.draw.rect(ventana, (60, 120, 200), boton_clasico, border_radius=24)
    pygame.draw.rect(ventana, (180, 90, 90), boton_avanzado, border_radius=24)

    txt_c = fuente_botones.render("Modo clásico", True, (255, 255, 255))
    txt_a = fuente_botones.render("Modo avanzado", True, (255, 255, 255))
    ventana.blit(txt_c, (boton_clasico.centerx - txt_c.get_width() // 2, boton_clasico.y + 20))
    ventana.blit(txt_a, (boton_avanzado.centerx - txt_a.get_width() // 2, boton_avanzado.y + 20))

    pygame.display.flip()
    return boton_clasico, boton_avanzado

def loop_juego(ventana, modo_avanzado: bool):
    reloj = pygame.time.Clock()
    fuente = pygame.font.SysFont(None, 28)
    gestor = GestorRecursos.get_instancia()
    gestor_memento = GestorMemento()
    fabrica_objetos = FabricaObjetos()
    pool_objetos = ObjectPoolObjetos(fabrica_objetos)

    fondo_mesa = gestor.obtener_imagen("fondo_mesa")

    cartas_j1 = crear_cartas_avanzadas() if modo_avanzado else crear_cartas_clasicas()
    cartas_j2 = crear_cartas_avanzadas() if modo_avanzado else crear_cartas_clasicas()

    jugador1 = Jugador("Jugador 1", cartas=cartas_j1)
    jugador2 = Jugador("Jugador 2", cartas=cartas_j2)

    turno_manager = TurnoManager([jugador1, jugador2], modo_avanzado)

    seleccion_dado = None
    mensaje_info = ""
    juego_terminado = False

    corriendo = True
    while corriendo:
        dt = reloj.tick(FPS)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return

            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                return

            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1 and not juego_terminado:
                mx, my = evento.pos
                jugador_act = turno_manager.turno_actual
                oponente = turno_manager.obtener_oponente()

                # Botones
                rect_reroll = pygame.Rect(40, ALTO_VENTANA - 100, 140, 48)
                rect_rest = pygame.Rect(200, ALTO_VENTANA - 100, 140, 48)
                rect_fin = pygame.Rect(360, ALTO_VENTANA - 100, 180, 48)

                if rect_reroll.collidepoint(mx, my) and modo_avanzado:
                    gestor_memento.guardar(jugador_act)
                    exito = jugador_act.hacer_reroll(modo_avanzado=True)
                    mensaje_info = "Reroll realizado." if exito else "No puedes rerollear."
                elif rect_rest.collidepoint(mx, my) and modo_avanzado:
                    if gestor_memento.restaurar(jugador_act):
                        mensaje_info = "Tirada restaurada."
                    else:
                        mensaje_info = "Nada que restaurar."
                elif rect_fin.collidepoint(mx, my):
                    turno_manager.pasar_turno()
                    seleccion_dado = None
                    mensaje_info = ""
                else:
                    # Selección de dados
                    dados_y = 200
                    for i, dado in enumerate(jugador_act.dados):
                        x = 80 + i * (DADO_TAM + 20)
                        y = dados_y
                        if pygame.Rect(x, y, DADO_TAM, DADO_TAM).collidepoint(mx, my):
                            seleccion_dado = i
                            mensaje_info = f"Seleccionado dado {i+1} (valor {dado.valor})."

                    # Selección de cartas
                    cartas_y = ALTO_VENTANA - CARTA_ALTO - 130
                    for idx, carta in enumerate(jugador_act.cartas):
                        cx = 80 + idx * (CARTA_ANCHO + 30)
                        cy = cartas_y
                        rect_c = pygame.Rect(cx, cy, CARTA_ANCHO, CARTA_ALTO)
                        if rect_c.collidepoint(mx, my) and seleccion_dado is not None:
                            if not carta.puede_usarse(jugador_act):
                                mensaje_info = "Esta carta ya fue usada este turno."
                                continue
                            dado = jugador_act.usar_dado(seleccion_dado)
                            if dado is None:
                                mensaje_info = "Dado inválido."
                                continue
                            potencia = dado.valor
                            contexto = {"pool_objetos": pool_objetos, "carta": carta, "mensaje": ""}
                            carta.estrategia.aplicar(jugador_act, oponente, potencia, contexto)
                            if not dado.es_fantasma:
                                carta.usada_en_turno = True
                            if contexto.get("mensaje"):
                                mensaje_info = contexto["mensaje"]
                            else:
                                mensaje_info = f"{jugador_act.nombre} usó {carta.nombre} con {potencia}."
                            if oponente.es_muerto():
                                mensaje_info = f"{jugador_act.nombre} ha ganado la partida."
                                juego_terminado = True
                            seleccion_dado = None

        # Dibujo
        if fondo_mesa is not None:
            ventana.blit(pygame.transform.smoothscale(fondo_mesa, (ANCHO_VENTANA, ALTO_VENTANA)), (0, 0))
        else:
            ventana.fill((20, 20, 30))

        jugador_act = turno_manager.turno_actual
        oponente = turno_manager.obtener_oponente()

        render_texto(ventana, f"Turno de: {jugador_act.nombre}", 40, 30, fuente)
        render_texto(ventana, f"{jugador1.nombre}: {jugador1.vida} HP", ANCHO_VENTANA - 260, 40, fuente)
        render_texto(ventana, f"{jugador2.nombre}: {jugador2.vida} HP", ANCHO_VENTANA - 260, 70, fuente)

        # Dibujar dados
        dados_y = 200
        for i, dado in enumerate(jugador_act.dados):
            x = 80 + i * (DADO_TAM + 20)
            y = dados_y
            dibujar_dado(ventana, GestorRecursos.get_instancia(), dado, x, y)
            if seleccion_dado == i:
                pygame.draw.rect(ventana, (255, 215, 0), (x-4, y-4, DADO_TAM+8, DADO_TAM+8), 3, border_radius=16)

        # Cartas
        cartas_y = ALTO_VENTANA - CARTA_ALTO - 130
        for idx, carta in enumerate(jugador_act.cartas):
            cx = 80 + idx * (CARTA_ANCHO + 30)
            cy = cartas_y
            dibujar_carta(ventana, GestorRecursos.get_instancia(), carta, cx, cy, fuente)

        # Botones
        rect_reroll = pygame.Rect(40, ALTO_VENTANA - 100, 140, 48)
        rect_rest = pygame.Rect(200, ALTO_VENTANA - 100, 140, 48)
        rect_fin = pygame.Rect(360, ALTO_VENTANA - 100, 180, 48)

        if modo_avanzado:
            pygame.draw.rect(ventana, (70, 140, 90), rect_reroll, border_radius=12)
            pygame.draw.rect(ventana, (90, 110, 170), rect_rest, border_radius=12)
            render_texto(ventana, "Reroll", rect_reroll.x + 32, rect_reroll.y + 14, fuente)
            render_texto(ventana, "Restaurar", rect_rest.x + 20, rect_rest.y + 14, fuente)
        else:
            pygame.draw.rect(ventana, (40, 40, 40), rect_reroll, border_radius=12)
            pygame.draw.rect(ventana, (40, 40, 40), rect_rest, border_radius=12)
            render_texto(ventana, "Reroll", rect_reroll.x + 32, rect_reroll.y + 14, fuente, (120, 120, 120))
            render_texto(ventana, "Restaurar", rect_rest.x + 20, rect_rest.y + 14, fuente, (120, 120, 120))

        pygame.draw.rect(ventana, (160, 70, 70), rect_fin, border_radius=12)
        render_texto(ventana, "Terminar turno", rect_fin.x + 10, rect_fin.y + 14, fuente)

        render_texto(ventana, mensaje_info, 40, 120, fuente, (255, 255, 255))

        pygame.display.flip()

def main():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
    pygame.display.set_caption(NOMBRE_JUEGO)

    gestor = GestorRecursos.get_instancia()
    # Intentar cargar assets base (si existen)
    try:
        gestor.cargar_imagen("fondo_menu", "assets/backgrounds/menu_bg.png")
    except FileNotFoundError:
        pass
    try:
        gestor.cargar_imagen("fondo_mesa", "assets/backgrounds/board_bg.png")
    except FileNotFoundError:
        pass

    # Cartas
    for tipo in ["ataque", "cura", "defensa", "objetos"]:
        try:
            gestor.cargar_imagen(f"carta_{tipo}", f"assets/cards/{tipo}.png")
        except FileNotFoundError:
            pass

    # Dados 1-8 y fantasma
    for i in range(1, 9):
        try:
            gestor.cargar_imagen(f"dado_{i}", f"assets/dice/die_{i}.png")
        except FileNotFoundError:
            pass

    reloj = pygame.time.Clock()
    estado = ESTADO_MENU
    corriendo = True

    while corriendo:
        if estado == ESTADO_MENU:
            botones = mostrar_menu(ventana, gestor)
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    corriendo = False
                elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                    mx, my = evento.pos
                    boton_clasico, boton_avanzado = botones
                    if boton_clasico.collidepoint(mx, my):
                        estado = ESTADO_CLASICO
                    elif boton_avanzado.collidepoint(mx, my):
                        estado = ESTADO_AVANZADO

        elif estado == ESTADO_CLASICO:
            loop_juego(ventana, modo_avanzado=False)
            estado = ESTADO_MENU

        elif estado == ESTADO_AVANZADO:
            loop_juego(ventana, modo_avanzado=True)
            estado = ESTADO_MENU

        reloj.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
