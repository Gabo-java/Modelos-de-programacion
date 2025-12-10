"""app.py
Juego principal en Pygame: Duelos por Dados 2.0
"""

import pygame

from configuracion import ANCHO, ALTO, FPS, NOMBRE_JUEGO
from gestor_recursos import GestorRecursos
from gestor_memento import GestorMemento
from carta import (
    Carta,
    EstrategiaAtaque,
    EstrategiaCura,
    EstrategiaDefensa,
    EstrategiaObjetos,
)
from fabrica_objetos import FabricaObjetos
from object_pool import ObjectPoolObjetos
from inventario import InventarioFacade 
from jugador import Jugador
from turno import TurnoManager


def crear_cartas_basicas():
    return [
        Carta("Ataque", "ataque", EstrategiaAtaque()),
        Carta("Cura", "cura", EstrategiaCura()),
        Carta("Defensa", "defensa", EstrategiaDefensa()),
        Carta("Objetos", "objetos", EstrategiaObjetos()),
    ]


def render_texto(superficie, texto, x, y, fuente, color=(255, 255, 255)):
    imagen = fuente.render(texto, True, color)
    superficie.blit(imagen, (x, y))


def main():
    pygame.init()
    pygame.display.set_caption(NOMBRE_JUEGO)
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()

    fuente = pygame.font.SysFont(None, 24)
    fuente_pequena = pygame.font.SysFont(None, 18)
    fuente_inventario = pygame.font.SysFont(None, 16)

    gestor_recursos = GestorRecursos.get_instancia()
    gestor_memento = GestorMemento()
    fabrica_objetos = FabricaObjetos()
    pool_objetos = ObjectPoolObjetos(fabrica_objetos)

    inventario_j1 = InventarioFacade(pool_objetos)
    inventario_j2 = InventarioFacade(pool_objetos)

    cartas_j1 = crear_cartas_basicas()
    cartas_j2 = crear_cartas_basicas()

    jugador1 = Jugador("Jugador 1", cartas=cartas_j1, inventario=inventario_j1)
    jugador2 = Jugador("Jugador 2", cartas=cartas_j2, inventario=inventario_j2)

    # Ventaja inicial para el jugador2
    for _ in range(2):
        inventario_j2.obtener_objeto_aleatorio_y_guardar("baja")

    turno_manager = TurnoManager([jugador1, jugador2])

    seleccion_dado = None
    seleccion_carta = None
    seleccion_objeto = None
    mensaje_info = ""
    juego_terminado = False

    #Debug-lista
    debug_calidades = ["baja", "media", "alta"]
    debug_index = 0

    corriendo = True
    while corriendo:
        dt = reloj.tick(FPS)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False
            
            #Debug
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_i:
                    jugador_act = turno_manager.turno_actual
                    calidad = debug_calidades[debug_index % len(debug_calidades)]
                    jugador_act.inventario.obtener_objeto_aleatorio_y_guardar(calidad)
                    debug_index += 1
            
            elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                if juego_terminado:
                    continue
                mx, my = evento.pos
                jugador_act = turno_manager.turno_actual
                oponente = turno_manager.obtener_oponente()

                # Botón Reroll
                if 20 <= mx <= 140 and 430 <= my <= 470:
                    gestor_memento.guardar(jugador_act)
                    exito = jugador_act.hacer_reroll()
                    if not exito:
                        mensaje_info = "No puedes rerollear (bloqueado o sin dados)."
                    else:
                        mensaje_info = "Reroll realizado."
                
                # Botón Restaurar
                elif 160 <= mx <= 280 and 430 <= my <= 470:
                    if gestor_memento.restaurar(jugador_act):
                        mensaje_info = "Tirada restaurada."
                    else:
                        mensaje_info = "Nada que restaurar."
                
                # Botón Terminar turno
                elif 310 <= mx <= 470 and 430 <= my <= 470:
                    turno_manager.pasar_turno()
                    seleccion_dado = None
                    seleccion_carta = None
                    seleccion_objeto = None
                    mensaje_info = ""
                
                else:
                    #Inventario
                    if 500 <= mx <= 880 and 300 <= my <= 530:
                        objetos = jugador_act.inventario.objetos_almacenados
                        for i in range(len(objetos)):
                            ox = 510
                            oy = 330 + i * 22 
                            if ox <= mx <= ox + 350 and oy <= my <= oy + 20:
                                if not jugador_act.objeto_usado_en_turno:
                                    exito, msg = jugador_act.inventario.usar_objeto(
                                        i, jugador_act, oponente, {}
                                    )
                                    mensaje_info = msg
                                    if exito and oponente.es_muerto():
                                        mensaje_info = f"{jugador_act.nombre} ha ganado."
                                        juego_terminado = True
                                else:
                                    mensaje_info = "Ya usaste un objeto este turno."
                                break
                    
                    # Selección de dados
                    for i, dado in enumerate(jugador_act.dados):
                        x = 20 + i * 60
                        y = 60
                        if x <= mx <= x + 50 and y <= my <= y + 50:
                            seleccion_dado = i
                            mensaje_info = f"Seleccionado dado {i+1} (valor {dado.valor})."

                    # Selección de cartas
                    for i, carta in enumerate(jugador_act.cartas):
                        cx = 20 + i * 210
                        cy = 150
                        if cx <= mx <= cx + 190 and cy <= my <= cy + 130:
                            if seleccion_dado is None:
                                seleccion_carta = i
                                mensaje_info = f"Carta seleccionada: {carta.nombre}."
                            else:
                                carta = jugador_act.cartas[i]
                                if not carta.puede_usarse(jugador_act):
                                    mensaje_info = (
                                        "Esa carta ya se usó este turno "
                                        "o ya se usó un objeto."
                                    )
                                    continue

                                dado = jugador_act.usar_dado(seleccion_dado)
                                if dado is None:
                                    mensaje_info = "El dado seleccionado no es válido."
                                    continue

                                potencia = dado.valor
                                contexto = {
                                    "pool_objetos": pool_objetos,
                                    "carta": carta,
                                    "mensaje": "",
                                }

                                carta.estrategia.aplicar(
                                    jugador_act, oponente, potencia, contexto
                                )

                                if not dado.es_fantasma:
                                    carta.usada_en_turno = True

                                if contexto.get("mensaje"):
                                    mensaje_info = contexto["mensaje"]
                                else:
                                    mensaje_info = (
                                        f"{jugador_act.nombre} usó "
                                        f"{carta.nombre} con {potencia}."
                                    )

                                if oponente.es_muerto():
                                    mensaje_info = (
                                        f"{jugador_act.nombre} ha ganado la partida."
                                    )
                                    juego_terminado = True

                                seleccion_dado = None
                                seleccion_carta = None

        ventana.fill((25, 25, 30))

        jugador_act = turno_manager.turno_actual
        oponente = turno_manager.obtener_oponente()

        render_texto(
            ventana,
            f"Turno de: {jugador_act.nombre}",
            20,
            20,
            fuente,
            color=(255, 255, 255),
        )

        render_texto(
            ventana,
            f"{jugador1.nombre}: {jugador1.vida} HP",
            650,
            40,
            fuente,
            color=(255, 255, 255),
        )
        render_texto(
            ventana,
            f"{jugador2.nombre}: {jugador2.vida} HP",
            650,
            70,
            fuente,
            color=(255, 255, 255),
        )

        # Dados actual
        for i, dado in enumerate(jugador_act.dados):
            x = 20 + i * 60
            y = 60
            color = (230, 230, 230)
            if seleccion_dado == i:
                color = (255, 215, 0)
            pygame.draw.rect(ventana, color, (x, y, 50, 50))
            valor_txt = str(dado.valor)
            if dado.es_fantasma:
                valor_txt += "F"
            render_texto(ventana, valor_txt, x + 15, y + 15, fuente, color=(0, 0, 0))

        # Cartas
        for i, carta in enumerate(jugador_act.cartas):
            cx = 20 + i * 210
            cy = 150
            estilos = carta.estilos()
            color_base = estilos["color_fondo"]
            color_borde = estilos["color_borde"]

            rect = pygame.Rect(cx, cy, 190, 130)
            fondo = color_base
            if carta.usada_en_turno or (
                carta.tipo == "objetos" and jugador_act.objeto_usado_en_turno
            ):
                fondo = (
                    int(color_base[0] * 0.4),
                    int(color_base[1] * 0.4),
                    int(color_base[2] * 0.4),
                )

            pygame.draw.rect(ventana, fondo, rect)
            pygame.draw.rect(ventana, color_borde, rect, 3)

            render_texto(
                ventana,
                carta.nombre,
                cx + 10,
                cy + 10,
                fuente,
                color=(255, 255, 255),
            )
            render_texto(
                ventana,
                carta.estrategia.descripcion_corta(),
                cx + 10,
                cy + 40,
                fuente_pequena,
                color=(230, 230, 230),
            )

        #Panel de inventario
        pygame.draw.rect(ventana, (40, 40, 50), (500, 300, 380, 230))
        pygame.draw.rect(ventana, (100, 100, 120), (500, 300, 380, 230), 2)
        render_texto(ventana, "INVENTARIO", 510, 305, fuente, color=(200, 200, 255))
        
        objetos = jugador_act.inventario.objetos_almacenados
        for i, obj in enumerate(objetos):
            ox = 510
            oy = 330 + i * 22  
            color_obj = (180, 180, 180)
            if obj.calidad == "baja":
                color_obj = (150, 150, 150)
            elif obj.calidad == "media":
                color_obj = (180, 180, 100)
            elif obj.calidad == "alta":
                color_obj = (220, 180, 50)
        
            render_texto(ventana, f"{i+1}. {obj.nombre}", ox, oy, fuente_inventario, color_obj)

        # Botones
        pygame.draw.rect(ventana, (80, 150, 80), (20, 430, 120, 40))
        render_texto(ventana, "Reroll", 40, 440, fuente)

        pygame.draw.rect(ventana, (80, 120, 200), (160, 430, 120, 40))
        render_texto(ventana, "Restaurar", 170, 440, fuente)

        pygame.draw.rect(ventana, (150, 50, 50), (310, 430, 160, 40))
        render_texto(ventana, "Terminar turno", 320, 440, fuente)

        render_texto(ventana, mensaje_info, 20, 320, fuente, color=(255, 255, 255))

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()