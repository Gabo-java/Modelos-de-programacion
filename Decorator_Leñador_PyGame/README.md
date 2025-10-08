# 🔥 Patrón de Diseño Decorator — Juego "Leñador" en Pygame

Este proyecto implementa el **patrón de diseño Decorator** en Python usando **Pygame**, aplicado a un videojuego donde un personaje puede adquirir pociones con efectos que alteran su comportamiento visual y funcional.

---

## 🎯 Objetivo

El propósito de este ejercicio es demostrar el uso del **patrón Decorator** para extender dinámicamente las funcionalidades de un objeto sin modificar su estructura original.  
En este caso, el objeto base es el **Personaje**, y los decoradores son las pociones que añaden o modifican sus capacidades durante el juego.

---

## ⚙️ Estructura del proyecto

├── app.py # Lógica principal del juego
├── personaje.py # Clase base del personaje
├── decoradores.py # Implementación del patrón Decorator
├── potis.py # Clase de pociones que aplican los decoradores
├── mundo.py # Genera el entorno del juego (árboles, pociones)
├── defaults.py # Constantes globales del proyecto
└── visuales.py # Elementos gráficos (árboles, sprites)


---

## 🧩 Patrón de diseño: Decorator

### 🧠 Descripción
El **patrón Decorator** permite añadir responsabilidades o comportamientos adicionales a un objeto de manera flexible y dinámica, envolviéndolo dentro de otro objeto decorador que extiende su funcionalidad.

En este juego, el patrón se implementa para que el **Personaje** pueda adquirir temporalmente poderes o mejoras al recoger pociones, sin alterar su clase original.

---

## 🧱 Estructura del patrón en el proyecto

| Elemento | Rol en el patrón Decorator | Descripción |
|-----------|-----------------------------|--------------|
| `Personaje` | **Componente concreto** | Clase base que representa al personaje principal del juego. |
| `Decorador` | **Clase abstracta decoradora** | Interfaz que mantiene una referencia al personaje y delega sus métodos. |
| `Aura`, `Velocidad`, `Fuego` | **Decoradores concretos** | Añaden comportamientos adicionales al personaje, como un aura visual, aumento de velocidad o una estela de fuego. |
| `Potis` | **Creador de decoradores** | Aplica el decorador correspondiente al personaje al recoger una poción. |

---

## 🔥 Ejemplo de aplicación del patrón

Cuando el personaje toma una poción:

```python
if self.tipo == 'fuego':
    return Fuego(personaje)

Esto crea una nueva instancia de Fuego, que envuelve al personaje existente.
El decorador Fuego redefine el método draw() para agregar una estela visual y puede alterar el movimiento si lo requiere, manteniendo el resto de comportamientos intactos.
🧩 Clases principales
Decorador

class Decorador:
    def __init__(self, personaje):
        self._personaje = personaje

    def move(self, dx, dy, mundo):
        result = self._personaje.move(dx, dy, mundo)
        return self

    def draw(self, pantalla):
        self._personaje.draw(pantalla)

Actúa como intermediario entre el personaje original y las nuevas funcionalidades.
Aura

Añade un efecto visual brillante alrededor del personaje:

class Aura(Decorador):
    def draw(self, pantalla):
        pygame.draw.circle(pantalla, (255, 204, 0, 22),
                           (self.x + self.tamaño//2, self.y + self.tamaño//2),
                           self.tamaño)
        self._personaje.draw(pantalla)

Velocidad

Aumenta la rapidez del movimiento según el nivel del personaje:

class Velocidad(Decorador):
    def move(self, dx, dy, mundo):
        multiplicador = 1.0 + (self.incremento_base * self.nivel_velocidad)
        return self._personaje.move(dx * multiplicador, dy * multiplicador, mundo)

Fuego

Deja una estela de fuego detrás del personaje en movimiento:

class Fuego(Decorador):
    def draw(self, pantalla):
        for x, y, _ in self.estela:
            pygame.draw.circle(pantalla, (255, 100, 0), (x, y), 4)
        self._personaje.draw(pantalla)

🎨 Ventajas del patrón Decorator

✅ Permite añadir nuevas funcionalidades sin modificar la clase original del personaje.
✅ Favorece la extensibilidad: se pueden crear nuevos efectos simplemente definiendo más decoradores.
✅ Promueve la reutilización de código y el principio abierto/cerrado (OCP) de la programación orientada a objetos.
✅ Permite combinar múltiples efectos (por ejemplo, un personaje con fuego y velocidad simultáneamente).



🚀 Requisitos

    Python 3.10 o superior

    Pygame 2.6.0 o superior

Instalación

pip install pygame

Ejecución

python app.py

👨‍💻 Créditos

    Programación base: Juan Sebastian Rodríguez Serrano, Gabriel Fernando Lozano Echeverry y Juan Sebastian Henriquez Berrios 

    Librerías: Pygame

📚 Licencia

Este ejercicio es de uso educativo y demostrativo para comprender el patrón de diseño Decorator en Python con Pygame.