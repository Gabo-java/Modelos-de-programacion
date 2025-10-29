# 🎰 Ruleta Bombástica

**Ruleta Bombástica** es un juego creado en **Python con Pygame** que pone a prueba la suerte de varios jugadores.  
Cada jugador debe activar una palanca… pero cuidado, ¡una de ellas activa la bomba y elimina al desafortunado!  
El último jugador en pie será el ganador.  

---

## 🧩 Características principales

- Implementa los **patrones de diseño**:
  - 🧠 **Command** → encapsula las acciones de los jugadores al activar palancas.
  - 🔗 **Chain of Responsibility (COR)** → gestiona el flujo de turnos entre jugadores.
- Sistema visual con **Pygame**.
- Interfaz simple y dinámica.
- Jugabilidad por turnos con mensajes de estado en pantalla.
- Modo **debug** (tecla `D`) para revelar la palanca bomba (solo para pruebas).

---

## 🕹️ Cómo jugar

1. Ejecuta el juego con:
   ```bash
   python app.py

    En cada turno, el jugador actual debe hacer clic en una palanca.

    Si la palanca activa la bomba, el jugador es eliminado.

    El turno pasa automáticamente al siguiente jugador vivo.

    El juego termina cuando solo queda un jugador con vida.

🧱 Estructura del proyecto

📁 RuletaBombastica
├── app.py                # Archivo principal: inicializa y ejecuta el juego
├── command.py            # Implementa el patrón Command
├── Controlador_juego.py  # Lógica central del juego
├── COR.py                # Implementa el patrón Chain of Responsibility
├── default.py            # Constantes y configuraciones globales
├── mundo.py              # Define los jugadores, palancas y funciones gráficas
└── README.md             # Documentación del proyecto

🧠 Patrones de diseño utilizados
1. Command Pattern (command.py)

Permite encapsular las acciones de los jugadores (como activar una palanca) dentro de objetos independientes.
Esto facilita agregar o modificar comandos sin alterar la lógica del juego.

class ComandoActivarPalanca(Comando):
    def ejecutar(self):
        return self.juego.activar_palanca(self.jugador, self.indice_palanca)

2. Chain of Responsibility (COR.py)

Controla el flujo de los turnos. Cada jugador sabe quién es el siguiente y delega el turno si está eliminado.

def manejar(self, juego):
    if self.jugador["vivo"]:
        juego.turno_actual = self.jugador
        juego.mostrar_mensaje(f"Turno de {self.jugador['nombre']}")
        return self
    else:
        return self.siguiente.manejar(juego)

🎨 Controles
Acción	Tecla / Click	Descripción
Activar palanca	🖱️ Click izquierdo	Intenta activar una palanca
Mostrar palanca bomba (debug)	D	Muestra visualmente la palanca que activa la bomba
Salir del juego	Cerrar ventana	Termina la partida
⚙️ Requisitos

    Python 3.9 o superior

    Pygame

Instalación de dependencias

pip install pygame

👾 Créditos

    Desarrollado en Python con Pygame.

    Implementa patrones de diseño clásicos en un contexto de juego interactivo.

    Proyecto académico/didáctico sobre lógica de juegos y diseño orientado a objetos.

