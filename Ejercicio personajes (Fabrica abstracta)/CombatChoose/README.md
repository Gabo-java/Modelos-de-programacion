# CombatChoose
Seleccion de personajes de combate


```markdown
# ⚔️ CombatChoose

Proyecto académico inspirado en los **Patrones de Diseño**, llevado a la web con **Flask (Python)**.  
Permite seleccionar una **raza** (Humano, Elfo, Orco o Enano) y ver sus características (Arma, Armadura, Cuerpo y Montura), con imágenes y descripciones dinámicas.

---

## 🚀 Requisitos

- [Python 3.10+](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installation/) (gestor de paquetes de Python)

---

## 📂 Organización del proyecto

```

CombatChoose/
│
├── app.py                   # Aplicación principal Flask
│
├── fabricas/                # Implementación del patrón Fábrica Abstracta
│   ├── **init**.py
│   ├── fabrica\_abstracta.py
│   ├── fabrica\_humanos.py
│   ├── fabrica\_elfos.py
│   ├── fabrica\_orcos.py
│   └── fabrica\_enanos.py
│
├── static/                  # Archivos estáticos
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── script.js
│   └── img/                 # Imágenes (armas, armaduras, cuerpos, monturas, fondos, etc.)
│
├── templates/               # Plantillas HTML (Jinja2)
│   ├── base.html
│   ├── index.html
│   └── seleccion.html
│
└── README.md

````

---

## ⚙️ Instalación y ejecución

1. **Clona este repositorio** o descárgalo como `.zip`:
   ```bash
   git clone https://github.com/tu-usuario/CombatChoose.git
   cd CombatChoose
````

2. **Crea un entorno virtual** (opcional pero recomendado):

   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux / Mac
   venv\Scripts\activate      # Windows
   ```

3. **Instala dependencias**:

   ```bash
   pip install flask
   ```

4. **Ejecuta la aplicación**:

   ```bash
   python app.py
   ```

5. Abre el navegador en:

   ```
   http://127.0.0.1:5000
   ```

---

## 🖼️ Funcionalidad

* En la página principal (`index`) se muestran **cartas** con las razas disponibles.
* Al seleccionar una raza, se abre una nueva página (`seleccion.html`) con:

  * **Arma** ⚔️
  * **Armadura** 🛡️
  * **Cuerpo** 🧍
  * **Montura** 🐎
    Cada elemento tiene su **descripción** (generada por la fábrica) y su **imagen correspondiente**.

---

## 📖 Conceptos aplicados

* **Patrón de Diseño Fábrica Abstracta**: separación de la creación de objetos según la familia de razas.
* **Arquitectura MVC simplificada** con Flask.
* **Templates con Jinja2**.
* **Frontend responsivo** con HTML + CSS.

---

## 👨‍💻 Autores

Proyecto desarrollado con fines educativos para practicar **diseño de software** y **aplicaciones web**.

Juan Sebastian Henriquez Berrios
Gabriel Fernando Lozano Echeverry
Juan Sebastian Rodriguez Serrano

```
