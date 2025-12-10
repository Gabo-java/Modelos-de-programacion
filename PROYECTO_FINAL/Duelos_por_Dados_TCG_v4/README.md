# 🎴 Duelos por Dados TCG – Versión Completa (Pygame)

Videojuego **1 vs 1 por turnos**, estilo **Trading Card Game**, desarrollado en **Python + Pygame**, con arquitectura modular y múltiples **patrones de diseño del GoF**.  
Cada jugador usa **dados, cartas y objetos** para derrotar al oponente.

Creado por: 

**Juan Sebastian Rodríguez Serrano**
**Gabriel Fernando Lozano Echeverry**
**Juan Sebastian Henriquez Berrios**

---

# 🕹️ Mecánicas principales

### 🎲 Dados
- Cada turno se generan **3 dados** (1–6).
- El jugador puede realizar **hasta 2 rerolls por turno**.
- Cada reroll:
  - Aumenta el valor de todos los dados en **+1 por cada reroll acumulado** (máx. 8).
  - Hace que el jugador **pierda 1 dado** en el siguiente turno (máx. penalización de 2).
  - Si usó al menos 1 reroll, en el **siguiente turno no podrá hacer reroll**.
- Antes del reroll se guarda el estado utilizando **Memento**, permitiendo restaurar la tirada.

---

# 🃏 Cartas disponibles (cada una solo se puede usar 1 vez por turno)

1. **Ataque**  
   Hace daño al enemigo igual al valor del dado + bonificaciones temporales.

2. **Cura**  
   Recupera vida igual al valor del dado.

3. **Defensa**  
   Obtiene escudo equivalente a `1 + valor del dado`.

4. **Objetos**  
   Usa Object Pool + Factory Method para generar objetos según el rango del dado:
   - **1–2** → Objeto de calidad **baja**  
   - **3–4** → Objeto de calidad **media**  
   - **5–8** → Objeto de calidad **alta**  
   Solo se puede usar **1 objeto por turno**.

---

# 🎒 Objetos del juego

Todos los objetos son de **un solo uso** en gameplay, pero internamente se reutilizan mediante **Object Pool** para optimizar memoria.

## 🟩 Calidad baja
1. **Aumento de ataque** → +2 al ataque ese turno.  
2. **Aumento de defensa** → +2 de escudo.  
3. **Bandita** → Cura 2 puntos de vida.

## 🟦 Calidad media
4. **Dados de plata** → Todos los dados +2.  
5. **Piromancia** → 2 de daño + DOT de 2 durante 3 turnos.  
6. **Pergamino de protección** → Cura 4 y da 2 de escudo.

## 🟨 Calidad alta
7. **Dados de oro** → Todos los dados +3.  
8. **Dado fantasma** → Añade un dado 4–8 que **no consume carta**.  
9. **Defensa absoluta** → Anula completamente los próximos **2 ataques** recibidos.

📌 El **Jugador 2** recibe 2 objetos aleatorios de calidad baja al iniciar la partida.

---

# 🧩 Patrones de diseño utilizados

Este proyecto implementa varios patrones del **GoF**:

## 🟦 Strategy  
**Ubicación:** `carta.py`  
Define el comportamiento de las cartas (Ataque, Cura, Defensa, Objetos).  
Permite agregar nuevas cartas sin modificar código existente.

## 🟦 Chain of Responsibility  
**Ubicación:** `turno.py`  
Gestiona las fases del turno: Inicio → Acciones → Fin.

## 🟦 Memento  
**Ubicación:** `gestor_memento.py`  
Permite guardar estados de tirada antes de un reroll y restaurarlos.

## 🟦 Factory Method  
**Ubicación:** `fabrica_objetos.py`  
Genera objetos según tipo sin acoplar el código a clases concretas.

## 🟦 Object Pool  
**Ubicación:** `object_pool.py`  
Reutiliza instancias de objetos para optimizar memoria y rendimiento.

## 🟦 Singleton  
**Ubicación:** `gestor_recursos.py`  
Garantiza que las imágenes y recursos solo se carguen una vez.

---

# ❌ Patrones que NO deben usarse aquí

## 🚫 Observer  
No existe un sistema de eventos complejo; sería sobreingeniería.

## 🚫 Mediator  
No hay múltiples módulos con comunicación caótica.

## 🚫 Abstract Factory  
No trabajamos con familias enteras de productos intercambiables.

## 🚫 Builder  
Los objetos no requieren procesos de construcción complejos.

## 🚫 Prototype  
No se necesitan clonaciones masivas de cartas u objetos.

## 🚫 Decorator  
Strategy cumple mejor la función de personalizar comportamiento.

---

# 🟧 Patrones que podrían usarse (pero no son necesarios)

## ✔ State  
Para modelar estados del juego (Menú, Combate, Fin).  
Actualmente se maneja con una FSM simple en `main.py`.

## ✔ Command  
Para permitir "deshacer" movimientos completos.  
No se implementó para evitar complejidad innecesaria.

## ✔ Template Method  
Alternativa válida a Chain of Responsibility, pero menos flexible.

## ✔ Flyweight  
Solo si se necesitaran miles de cartas/dados simultáneos, lo cual no ocurre.

---

# 📁 Estructura del proyecto

Duelos_por_Dados_TCG/
│
├── main.py
├── configuracion.py
├── carta.py
├── jugador.py
├── turno.py
├── objeto.py
├── object_pool.py
├── fabrica_objetos.py
├── gestor_recursos.py
├── gestor_memento.py
│
└── assets/
├── cards/
├── dice/
└── backgrounds/


---

# 🎨 Tamaños recomendados para assets

| Asset             | Tamaño recomendado |
|------------------|-------------------|
| Cartas TCG        | `220 × 320 px` |
| Dado base         | `96 × 96 px` |
| Fondos del juego  | `1280 × 720 px` |

---

# 🏁 Conclusión

**Duelos por Dados TCG** es un proyecto modular, escalable y completamente extensible, ideal para aprender:

✔ Patrones de diseño  
✔ Arquitectura de videojuegos  
✔ Manejo de recursos  
✔ Sistemas de combate por turnos  
✔ Programación orientada a objetos  


Listo para expandirse con:
- Nuevas cartas  
- Objetos adicionales  
- Nuevos modos de juego  
- Tableros y skins personalizados  

