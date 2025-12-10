# 🎲 Duelos por Dados 2.0 (Pygame)

Este proyecto es un videojuego **1 vs 1 por turnos** desarrollado en **Python + Pygame**, donde cada jugador utiliza **dados y cartas** para atacarse, curarse, defenderse y activar objetos especiales.

---

## 🕹️ Mecánicas principales

- Cada turno, el jugador obtiene **3 dados** (1–6).
- Puede hacer hasta **2 rerolls por turno**:
  - Cada reroll mejora el rango de los dados en **+1** (hasta 8).
  - Por cada reroll, el jugador **pierde 1 dado en el siguiente turno** (máx. 2).
  - Si usó algún reroll en un turno, en el **siguiente turno no puede usar reroll** (bloqueo por un turno).
  - Antes del reroll se guarda el estado con **Memento** y se puede restaurar.

- Cartas (cada una solo se puede usar **1 vez por turno**):
  1. **Ataque** → hace daño al enemigo igual al valor del dado (+ buffs).
  2. **Cura** → recupera vida igual al valor del dado.
  3. **Defensa** → otorga un escudo de `1 + dado` durante 1 turno.
  4. **Objetos** → genera un objeto aleatorio según el valor del dado y lo aplica:
     - 1–2 → calidad **baja**
     - 3–4 → calidad **media**
     - 5–8 → calidad **alta**

- Solo se puede usar **1 objeto por turno**.

---

## 🎒 Objetos

Todos los objetos son de **un solo uso** en el juego, pero se reutilizan internamente con un **Object Pool**.

### Calidad baja
1. **Aumento de ataque**: `+2` al ataque durante el turno.
2. **Aumento de defensa**: `+2` de escudo.
3. **Bandita**: cura `2` de vida.

### Calidad media
4. **Dados de plata**: todos los dados del turno reciben `+2`.
5. **Piromancia**: daño de `2` inmediato + DOT de `2` durante **3 turnos**.
6. **Pergamino de protección**: cura `4` y da `2` de escudo.

### Calidad alta
7. **Dados de oro**: todos los dados del turno reciben `+3`.
8. **Dado fantasma**: añade un dado `4–8` que **no consume la carta usada**.
9. **Defensa absoluta**: anula completamente los próximos **2 ataques** recibidos.

Además, al **Jugador 2** se le otorgan 2 objetos aleatorios de calidad baja al iniciar la partida.

---

## 🧩 Patrones de diseño usados

### 1. Strategy – comportamiento de cartas (`carta.py`)

- **Dónde:** clases `EstrategiaAtaque`, `EstrategiaCura`, `EstrategiaDefensa`, `EstrategiaObjetos`.
- **Por qué:** cada carta tiene un comportamiento distinto, pero se usa mediante una interfaz común:
  ```python
  carta.estrategia.aplicar(actor, objetivo, potencia, contexto)

    Ventajas: permite añadir nuevas cartas sin modificar el código de jugadores ni del bucle principal (principio Open/Closed).

Alternativas posibles pero menos adecuadas:

    Template Method: impondría una estructura fija a los pasos, poco flexible para efectos tan diferentes.

    State: está pensado para representar estados persistentes, no acciones puntuales.

### 2. Chain of Responsibility – fases del turno (turno.py)

    **Dónde:** InicioTurnoHandler, AccionHandler, FinTurnoHandler y TurnoManager.

    **Por qué:** un turno se compone de fases encadenadas:

        inicio → acción → fin.

    Cada handler se encarga de una responsabilidad:

    InicioTurnoHandler -> AccionHandler -> FinTurnoHandler

    Ventajas: es fácil agregar nuevas fases (por ejemplo, “resolución de DOTs globales”, “eventos especiales”) sin romper las existentes.

Alternativas menos adecuadas:

    Observer: los turnos no son simples eventos, sino un flujo ordenado obligatorio.

    Mediator: haría un objeto central excesivamente complejo sin aportar ventajas claras.

### 3. Memento – tiradas de dados y reroll (gestor_memento.py)

    **Dónde:** MementoTirada y GestorMemento.

    **Por qué:** antes de hacer un reroll se crea un snapshot del estado:

        valores de los dados,

        rerolls realizados,

        penalización de dados del próximo turno.

    Si el jugador no está conforme con el reroll, puede restaurar la tirada anterior.

Ventajas:

    Permite implementar undo sin romper el encapsulamiento de Jugador.

Alternativas:

    Command: también permite undo, pero obliga a modelar cada acción como comando; aquí el estado es complejo y se vuelve más verboso.

    Prototype: solo clona, pero no gestiona pilas ni historial.

### 4. Object Pool – gestión de objetos (object_pool.py)

    **Dónde:** ObjectPoolObjetos.

    **Por qué:** los objetos se crean, usan y descartan constantemente. En vez de instanciar y destruir todo el rato:

        se mantiene un pool de instancias reutilizables por tipo.

        cuando se necesita un objeto de cierta calidad, se pide al pool.

        tras usarlo en el juego, se resetea y vuelve al pool.

Ventajas:

    Eficiencia (menos garbage).

    Control centralizado de los tipos de objetos disponibles.

Alternativas:

    Flyweight: más enfocado en compartir estado inmutable; aquí los objetos tienen comportamiento y duración.

    Prototype: serviría para clonar, pero no resuelve la reutilización ni la gestión de disponibilidad.

### 5. Factory Method – creación de objetos (fabrica_objetos.py)

    **Dónde:** FabricaObjetos.crear_objeto(tipo).

    **Por qué:** encapsula la lógica de creación de cada objeto según su tipo:

    fabrica.crear_objeto("dados_oro")

    Ventajas: si se añade un nuevo objeto, solo se modifica la fábrica, manteniendo el resto del código estable.

Alternativas:

    Abstract Factory: tendría sentido si hubiera familias completas coherentes (por ejemplo, “fábrica de objetos de fuego”, “fábrica de objetos de hielo”). Aquí la complejidad sería innecesaria.

    Builder: no se necesita construcción paso a paso, los objetos son simples.

6. Singleton – gestor de recursos (gestor_recursos.py)

    **Dónde:** GestorRecursos.

    **Por qué:** la carga de imágenes y sonidos es un servicio global y solo debería haber una instancia compartida.

❌ Patrones que NO se deberían usar aquí

    Singleton para Jugador, Cartas u Objetos: rompería el concepto de múltiples instancias (2 jugadores, muchas cartas, muchos objetos).

    State para cartas: las cartas no representan estado permanente, sino acciones puntuales ligadas a un dado.

    Mediator para turnos: complicaría el diseño centralizando demasiado la lógica de interacción.

    Observer para rerolls: el reroll es una acción directa del jugador, no un evento distribuido.

🚀 Ejecución

    Instalar dependencias:

pip install pygame

    Ejecutar el juego:

python main.py

