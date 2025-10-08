import pygame
import defaults
import os

class Personaje:
    def __init__(self, x, y):
        self.x=x
        self.y=y
        self.tamaño=defaults.PERSONAJEHB
        self.inventario={"madera": 0}
        personaje_path=os.path.join('assets', 'imagenes', 'personaje', 'personaje.png')
        self.sprite_sheet=pygame.image.load(personaje_path).convert_alpha()
        
        self.frame_tamaño=defaults.ANIMACION_FRAMES
        self.animacion_frame=0
        self.animacion_timer=0  
        self.animacion_delay=defaults.ANIMACION_DELAY
        self.estado_actual=defaults.QUIETO_ABAJO
        self.se_mueve=False
        self.por_izquierda=False
        self.direccion="abajo"  

        self.animaciones=self.carga_animaciones()
        self.imagen=self.animaciones[self.estado_actual][0]  # 

    def carga_animaciones(self):
        animaciones={}
        for estado in range(defaults.CUADROSANIMACION):
            frames=[]
            for frame in range(defaults.CUADROSANIMACION):
                surface=pygame.Surface((self.frame_tamaño, self.frame_tamaño), pygame.SRCALPHA)
                surface.blit(self.sprite_sheet, (0, 0), 
                           (frame*self.frame_tamaño, 
                            estado*self.frame_tamaño, 
                            self.frame_tamaño, 
                            self.frame_tamaño))
                surface=pygame.transform.scale(surface, (defaults.PERSONAJEAL, defaults.PERSONAJEAN))
                frames.append(surface)
            animaciones[estado]=frames
        return animaciones

    def actualizar_animacion(self, dt):
        self.animacion_timer+=dt
        
        if self.animacion_timer>=self.animacion_delay:
            self.animacion_timer=0
            self.animacion_frame=(self.animacion_frame +1) % defaults.CUADROSANIMACION
            self.imagen=self.animaciones[self.estado_actual][self.animacion_frame]
            return self

    def actualizar_estado_animacion(self, dx, dy):
      
        if dx==0 and dy==0:
            
            if self.direccion=="arriba":
                self.estado_actual=defaults.QUIETO_ARRIBA
            elif self.direccion=="abajo":
                self.estado_actual=defaults.QUIETO_ABAJO
            elif self.direccion=="derecha":
                self.estado_actual=defaults.QUIETO_DERECHA
            elif self.direccion=="izquierda":
                self.estado_actual=defaults.QUIETO_DERECHA 
        else:
          
            if dy<0:
                self.direccion="arriba"
                self.estado_actual=defaults.CAMINAR_ARRIBA
            elif dy>0:
                self.direccion="abajo"
                self.estado_actual=defaults.CAMINAR_ABAJO
            elif dx > 0:
                self.direccion="derecha"
                self.estado_actual=defaults.CAMINAR_DERECHA
            elif dx < 0:
                self.direccion="izquierda"
                self.estado_actual=defaults.CAMINAR_DERECHA  

    def draw(self, pantalla):
        
        if self.direccion=="izquierda":
            imagen_flip=pygame.transform.flip(self.imagen, True, False)
            pantalla.blit(imagen_flip, (self.x, self.y))
        else:
            pantalla.blit(self.imagen, (self.x, self.y))

    def move(self, dx, dy, mundo):
        x=self.x + dx
        y=self.y + dy

        for arbol in mundo.arboles:
            if self.colision(x, y, arbol):
                return self  

        self.x=x
        self.y=y
           
        self.x=max(0, min(self.x, defaults.ANCHO - self.tamaño))
        self.y=max(0, min(self.y, defaults.ALTO - self.tamaño))
    
        self.actualizar_estado_animacion(dx, dy)
        return self  

    def colision(self, x, y, objeto):
        return (x<objeto.x +objeto.size and 
                x +self.tamaño >objeto.x and 
                y <objeto.y +objeto.size and 
                y +self.tamaño >objeto.y)

    def cerca(self, objeto):
        return (abs(self.x -objeto.x)<=max(self.tamaño, objeto.size) +6 and 
                abs(self.y -objeto.y)<=max(self.tamaño, objeto.size) +6)
    
    def interactuar(self, mundo):
        for arbol in mundo.arboles:
            if self.cerca(arbol):
                if arbol.talar():  
                    self.inventario['madera']+=1
                    if arbol.madera==0:
                        mundo.arboles.remove(arbol)
                return