import pygame, random
from default import *
from mundo import jugadores, palancas, colores_palancas, dibujar_bomba
from COR import ManejadorJugador

#Contiene la logica del juego 
class ControladorJuego:
    def __init__(self, pantalla):
        self.pantalla=pantalla
        self.cadena_jugadores=[]
        self.turno_actual=None
        self.palanca_bomba=random.choice(palancas)
        self.debug_activo=False  
        self.mensaje=""
        self.palancas_activas=[True for _ in palancas]
        self.crear_cadena_jugadores()

    def crear_cadena_jugadores(self):
        anterior=None
        for jugador in jugadores:
            handler=ManejadorJugador(jugador)
            if anterior:
                anterior.establecer_siguiente(handler)
            else:
                self.cadena_jugadores.append(handler)
            anterior=handler
        anterior.establecer_siguiente(self.cadena_jugadores[0])

    def mostrar_mensaje(self, texto):
        self.mensaje=texto

    def activar_palanca(self, jugador, indice):
        palanca = palancas[indice]
        if not self.palancas_activas[indice]:
            self.mostrar_mensaje("Esa palanca ya fue usada.")
            self.actualizar_pantalla()
            pygame.time.delay(DELAY_MENSAJE)
            return False

        self.palancas_activas[indice]=False
        self.mostrar_mensaje("La bomba va a...")
        self.actualizar_pantalla()
        pygame.time.delay(DELAY_MENSAJE)

        if palanca is self.palanca_bomba:
            self.mostrar_mensaje("a explotar en 2 segundos.")
            self.actualizar_pantalla()
            pygame.time.delay(DELAY_EXPLOSION)
            self.explotar(jugador, indice)
        else:
            self.mostrar_mensaje("No va a explotar.")
            self.actualizar_pantalla()
            pygame.time.delay(DELAY_MENSAJE)
        return True

    def explotar(self, jugador, indice):
        jugador["vivo"]=False
        self.mostrar_mensaje(f"{jugador['nombre']} ha sido eliminado.")
        self.actualizar_pantalla()
        pygame.time.delay(DELAY_ELIMINADO)
                          
        del palancas[indice]
        del colores_palancas[indice]
        del self.palancas_activas[indice]

        if palancas:
            self.palanca_bomba=random.choice(palancas)
            self.palancas_activas=[True for _ in palancas]

    def siguiente_turno(self, handler_actual):
        return handler_actual.siguiente.manejar(self)

    def hay_ganador(self):
        vivos=[j for j in jugadores if j["vivo"]]
        return vivos[0] if len(vivos)==1 else None

    def actualizar_pantalla(self):
        self.pantalla.fill((30, 30, 30))
        dibujar_bomba(self.pantalla)

        #Se encarga de dibujar a los jugadores
        for j in jugadores:
            color=j["color"] if j["vivo"] else GRIS
            pygame.draw.circle(self.pantalla, color, j["pos"], RADIO_JUGADOR)
            texto=FUENTE.render(j["nombre"], True, NEGRO)
            self.pantalla.blit(texto, (j["pos"][0]-20, j["pos"][1]-21))

        #Se encargad de dibujar las palancas
        for i, palanca in enumerate(palancas):
            color=colores_palancas[i] if self.palancas_activas[i] else GRIS_OSCURO
            pygame.draw.rect(self.pantalla, color, palanca)

            #Texto para pruebas 
            if self.debug_activo and palanca is self.palanca_bomba:
                cx=palanca.centerx
                y=palanca.y-40
                pygame.draw.polygon(self.pantalla, BLANCO, [(cx, y), (cx-15, y+25), (cx+15, y+25)])
                pygame.draw.line(self.pantalla, AMARILLO, (cx, y-10), (cx, y), 3)

        #Se encarga de los textos en pantalla
        if self.mensaje:
            texto=FUENTE.render(self.mensaje, True, BLANCO)
            self.pantalla.blit(texto, (ANCHO //2-80, 225))

        pygame.display.flip()