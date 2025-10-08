# 🌲 Leñador — Juego en Pygame

**Leñador** es un videojuego desarrollado con **Python y Pygame** en el que el jugador controla a un personaje que puede moverse, talar árboles y recoger pociones con diferentes efectos visuales y de velocidad.  
El juego fue diseñado para demostrar la aplicación de **patrones de diseño** y buenas prácticas de programación orientada a objetos en entornos interactivos.

---

## 🎮 Características principales

- Movimiento del personaje con **patrón de diseño Adapter**:
  - Control por **teclado** (flechas direccionales).
  - Control por **mouse** (el personaje se mueve hacia el cursor).
  - Cambio dinámico de control con la tecla `C`.
- Interacción con el entorno:
  - Talar árboles para recolectar madera.
  - Tomar pociones con efectos de **Aura**, **Velocidad** y **Fuego**.
- Decoradores que aplican efectos visuales y funcionales al personaje.
- Sistema de animaciones, inventario y reaparición de objetos.

---

## ⚙️ Estructura del proyecto

├── app.py # Bucle principal del juego y control del personaje
├── control_adapter.py # Implementación del patrón Adapter (teclado y mouse)
├── personaje.py # Clase base del personaje y sus animaciones
├── mundo.py # Generación del mapa, árboles y pociones
├── potis.py # Clase de pociones y aplicación de efectos
├── decoradores.py # Implementación de los efectos (Aura, Velocidad, Fuego)
├── visuales.py # Representación gráfica de árboles y objetos
├── defaults.py # Constantes globales (colores, tamaños, animaciones, etc.)
└── assets/ # Carpeta con imágenes y recursos gráficos


---

## 🧠 Patrón de diseño usado: Adapter

El **Adapter Pattern** permite integrar diferentes métodos de control (teclado o mouse) sin alterar la lógica del personaje.  
Esto se logra mediante la interfaz `ControlAdapter`, que define un método genérico `obtener_movimiento()`, implementado por:

- `TecladoAdapter`: interpreta las teclas de dirección.
- `MouseAdapter`: calcula el desplazamiento hacia el cursor.

Este enfoque hace que el juego sea extensible y fácilmente adaptable a nuevos dispositivos de entrada, como controladores o IA.

---

## 💡 Patrones adicionales

El juego también utiliza el **patrón Decorator**, aplicado en las clases de efectos (`Aura`, `Velocidad`, `Fuego`), para añadir comportamientos y características al personaje sin modificar su clase base.

---

## 🧾 Documentación del código

La documentación interna del código (docstrings, explicaciones y comentarios) fue elaborada por **ChatGPT (GPT-5)** a solicitud del autor del proyecto.  
La documentación detalla:
- La estructura del juego.
- La relación entre los módulos.
- El propósito de cada clase y método.
- Los principios de diseño aplicados.

> 📝 *ChatGPT (GPT-5) generó y redactó la documentación técnica del código fuente, siguiendo el estándar PEP 257 para docstrings y buenas prácticas de claridad estructural.*

---

## 🚀 Requisitos

- Python 3.10 o superior  
- Pygame 2.6.0 o superior

### Instalación
```bash
pip install pygame

Ejecución

python app.py

🎨 Créditos

    Programación base: Juan Sebastian Rodríguez Serrano, Gabriel Fernando Lozano Echeverry y Juan Sebastian Henriquez Berrios 

    Documentación Docstrings estilo PEP 257: ChatGPT (GPT-5)

    Librerías: Pygame

    Recursos visuales: Carpeta assets/imagenes (sprites, fondo, objetos).

📚 Licencia

Este proyecto se distribuye con fines educativos y de demostración de patrones de diseño en Python.
Puedes modificar y usar el código citando la fuente original.