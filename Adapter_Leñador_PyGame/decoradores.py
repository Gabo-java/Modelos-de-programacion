import pygame
import defaults
import random
import time

class Decorador:
    def __init__(self, personaje):
        self._personaje=personaje
        self.tiempo_ultimo_efecto=time.time()
    
    def __getattr__(self, name):
        return getattr(self._personaje, name)
    
    def draw(self, pantalla):
        self._personaje.draw(pantalla)
    
    def move(self, dx, dy, mundo):
        result=self._personaje.move(dx, dy, mundo)
        if result is not None and result!=self._personaje:
            self._personaje = result
        return self
    
    def actualizar_animacion(self, dt):
        self._personaje.actualizar_animacion(dt)
    
    def interactuar(self, mundo):
        return self._personaje.interactuar(mundo)

class Aura(Decorador):
    def __init__(self, personaje):
        super().__init__(personaje)
        self.nivel_aura = 1
        if hasattr(personaje, 'nivel_aura'):
            self.nivel_aura = personaje.nivel_aura + 1
        self.tiempo_ultimo_efecto = time.time()
        if not hasattr(personaje, 'pociones_aura'):
            personaje.pociones_aura=0
        personaje.pociones_aura+=1
    
    def draw(self, pantalla):
        radio_base = self.tamaño // 2 
        for i in range(self.nivel_aura):
            radio = radio_base + (i * defaults.AUMENTOAU)
            aura_rect = pygame.Rect(
                self.x + (self.tamaño - radio * 2) // 2,
                self.y + (self.tamaño - radio * 2) // 2,
                radio * 2,
                radio * 2
            )
            
            aura_surface=pygame.Surface((radio*2, radio*2), pygame.SRCALPHA)
            pygame.draw.circle(aura_surface, defaults.COLORAU, (radio, radio), radio)
            pantalla.blit(aura_surface, aura_rect)
        
        self._personaje.draw(pantalla)
    
    def indicador(self, pantalla):
        font=pygame.font.SysFont("Comic Sans MS", 15)
        texto=font.render(f"Aura {self.nivel_aura}", True, defaults.POCIONAU)
        pantalla.blit(texto, (self.x, self.y-15))

class Velocidad(Decorador):
    def __init__(self, personaje):
        super().__init__(personaje)
        self.incremento_base=defaults.AUMENTOVEL
        self.nivel_velocidad=1
        
        if hasattr(personaje, 'nivel_velocidad'):
            self.nivel_velocidad=personaje.nivel_velocidad + 1
        self.tiempo_ultimo_efecto=time.time()
        if not hasattr(personaje, 'pociones_velocidad'):
            personaje.pociones_velocidad = 0
        personaje.pociones_velocidad += 1
    
    def move(self, dx, dy, mundo):
        multiplicador=1.0+(self.incremento_base * self.nivel_velocidad)
        dx_super=dx*multiplicador
        dy_super=dy*multiplicador
        
        result = self._personaje.move(dx_super, dy_super, mundo)
        if result is not None and result!=self._personaje:
            self._personaje=result
        return self
    
    def indicador(self, pantalla):
        velocidad_actual=1.0+(self.incremento_base * self.nivel_velocidad)
        font=pygame.font.SysFont("Comic Sans MS", 15)
        texto=font.render(f"Vel x{velocidad_actual:.2f}", True, defaults.POCIONVEL)
        pantalla.blit(texto, (self.x, self.y-15))

class Fuego(Decorador):
    def __init__(self, personaje):
        super().__init__(personaje)
        self.nivel_fuego=1
        self.duracion_base=0.5
        self.incremento_duracion=defaults.AUMENTOFUE
        self.estela=[]

        if hasattr(personaje, 'nivel_fuego'):
            self.nivel_fuego = personaje.nivel_fuego + 1
            if hasattr(personaje, 'estela'):
                self.estela=personaje.estela
        self.tiempo_ultimo_efecto=time.time()
        if not hasattr(personaje, 'pociones_fuego'):
            personaje.pociones_fuego=0
        personaje.pociones_fuego+=1

        self.ultima_posicion=(self.x, self.y)

    
    @property
    def duracion_total(self):
        return self.duracion_base+(self.incremento_duracion*(self.nivel_fuego-1))
    
    def move(self, dx, dy, mundo):
        self.actualizar_estela()
        nueva_x=self.x+dx
        nueva_y=self.y+dy
        if (nueva_x, nueva_y)!=(self.x, self.y):
            self.estela.append((self.x + self.tamaño//2, self.y + self.tamaño//2, time.time()))
            self.ultima_posicion=(self.x, self.y)
        
        result=self._personaje.move(dx, dy, mundo)
        if result is not None and result != self._personaje:
            self._personaje=result
        
        return self
    
    def actualizar_estela(self):
        tiempo_actual=time.time()
        self.estela=[(x, y, t) for x, y, t in self.estela 
                      if tiempo_actual - t < self.duracion_total]
    
    def draw(self, pantalla):
        tiempo_actual = time.time()
        for x, y, tiempo_creacion in self.estela:
            tiempo_transcurrido=tiempo_actual - tiempo_creacion
            progreso=tiempo_transcurrido / self.duracion_total
            
            tamaño=max(2, int(6 * (1 - progreso)))
            color=defaults.ROJO
            pygame.draw.circle(pantalla, color, (int(x), int(y)), tamaño)

        self._personaje.draw(pantalla)
         
    def draw_indicador_permanente(self, pantalla):
        font=pygame.font.SysFont("Comic Sans MS", 15)
        texto=font.render(f"Fuego {self.nivel_fuego}", True, defaults.POCIONFUE)
        pantalla.blit(texto, (self.x, self.y-15))