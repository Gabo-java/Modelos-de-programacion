# 🧙‍♂️ Duelos por Dados - Versión Mejorada

**Duelos por Dados** es un juego por turnos hecho con **Python y Pygame**, donde dos jugadores se enfrentan usando **cartas y dados**.  
Cada carta tiene un efecto distinto (ataque, cura o defensa), y el resultado depende del valor del dado elegido.  
El proyecto aplica varios **patrones de diseño clásicos** de forma educativa y práctica.

---

## 🎯 Objetivo del juego
Derrotar al oponente reduciendo su vida a 0 mediante el uso estratégico de tus cartas y dados.

Cada turno, los jugadores pueden:
- **Rerollear** sus dados hasta 2 veces.
- **Usar un dado** para activar el efecto de una carta.
- **Curarse o defenderse** según la estrategia elegida.
- **Terminar su turno** y pasar al oponente.

---

## 🧩 Patrones de diseño implementados

| Patrón | Archivo | Descripción |
|--------|----------|-------------|
| **Strategy** | `carta.py` | Define el comportamiento de cada tipo de carta (ataque, cura, defensa). |
| **Factory Method** | `fabrica_cartas.py` | Crea cartas según su tipo con la estrategia adecuada. |
| **Memento** | `gestor_memento.py` | Guarda y restaura el estado de los dados antes de un reroll. |
| **Singleton** | `gestor_recursos.py` | Gestiona la carga única de imágenes y sonidos en todo el juego. |
| **Chain of Responsibility** | `turno.py` | Controla el flujo del turno entre los distintos jugadores. |

---

## ⚙️ Estructura del proyecto

```
📁 duelos_por_dados/
├── carta.py               # Patrón Strategy: comportamiento de las cartas
├── configuracion.py       # Constantes del juego
├── fabrica_cartas.py      # Patrón Factory Method para crear cartas
├── gestor_memento.py      # Patrón Memento: guarda y restaura estados
├── gestor_recursos.py     # Patrón Singleton: manejo de recursos (imágenes/sonidos)
├── jugador.py             # Lógica del jugador, dados y objetos
├── turno.py               # Patrón Chain of Responsibility: flujo de turnos
└── main.py                # Punto de entrada del juego (interfaz pygame)
```

---

## 🕹️ Controles y mecánicas básicas

| Acción | Cómo hacerlo |
|--------|---------------|
| 🎲 **Reroll** | Click en el botón “Reroll” (máx. 2 veces por turno). |
| ♻️ **Restaurar tirada** | Click en “Restaurar” para deshacer el último reroll (usa Memento). |
| ⚔️ **Usar carta** | Selecciona un dado y luego una carta para aplicarla. |
| 🏁 **Terminar turno** | Click en “Terminar Turno”. |
| ❤️ **Curarse** | Usa la carta de tipo “Cura”. |
| 🛡️ **Defenderse** | Usa la carta de tipo “Defensa”. |
| ☠️ **Atacar** | Usa la carta de tipo “Ataque” para dañar al oponente. |

---

## 🧠 Lógica de juego

- **Ataque** → Daño directo igual al valor del dado.  
- **Cura** → Recupera vida igual al valor del dado.  
- **Defensa** → Cura parcial (la mitad del dado).  
- Cada **reroll** aumenta la potencia de las nuevas tiradas (+1 por reroll).  
- Si un jugador realiza rerolls, puede perder dados el siguiente turno.

---

## 🚀 Ejecución

### Requisitos previos
- Python 3.9 o superior  
- Librería `pygame`

### Instalación
```bash
pip install pygame
```

### Ejecución del juego
```bash
python main.py
```

---

## 🧱 Extensiones posibles

- Implementar **nuevas cartas** con estrategias personalizadas (usando `EstrategiaCarta`).  
- Añadir **efectos visuales o sonidos** con `GestorRecursos`.  
- Incorporar **modo IA** para jugar contra la computadora.  
- Crear **objetos consumibles** más avanzados en `jugador.py`.  

---

## 👨‍💻 Autor

Proyecto desarrollado con fines académicos y de práctica de patrones de diseño.  
Creado por **Juan Sebastian Rodríguez Serrano, Gabriel Fernando Lozano Echeverry y Juan Sebastian Henriquez Berrios**.  
Universidad Distrital Francisco José de Caldas – Ingeniería de Sistemas.  
