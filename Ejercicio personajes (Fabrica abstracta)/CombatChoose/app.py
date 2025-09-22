from flask import Flask, render_template, jsonify
from fabricas.fabrica_humanos import FabricaHumanos
from fabricas.fabrica_elfos import FabricaElfos
from fabricas.fabrica_orcos import FabricaOrcos
from fabricas.fabrica_enanos import FabricaEnanos

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/seleccionar/<raza>")
def seleccionar_raza(raza):
    fabricas = {
        "humano": FabricaHumanos(),
        "elfo": FabricaElfos(),
        "orco": FabricaOrcos(),
        "enano": FabricaEnanos()
    }

    if raza.lower() not in fabricas:
        return render_template("seleccion.html", error="Raza no encontrada")

    fabrica = fabricas[raza.lower()]
    datos = {
        "raza": raza.capitalize(),
        "arma": {
            "desc": fabrica.crear_arma().get_descripcion(),
            "img": f"arma_{raza.lower()}.png"
        },
        "armadura": {
            "desc": fabrica.crear_armadura().get_descripcion(),
            "img": f"armadura_{raza.lower()}.png"
        },
        "cuerpo": {
            "desc": fabrica.crear_cuerpo().get_descripcion(),
            "img": f"{raza.lower()}.png"
        },
        "montura": {
            "desc": fabrica.crear_montura().get_descripcion(),
            "img": f"montura_{raza.lower()}.png"
        }
    }

    return render_template("seleccion.html", datos=datos)


@app.route("/api/seleccionar/<raza>")
def api_seleccionar_raza(raza):
    fabricas = {
        "humano": FabricaHumanos(),
        "elfo": FabricaElfos(),
        "orco": FabricaOrcos(),
        "enano": FabricaEnanos()
    }

    if raza.lower() not in fabricas:
        return jsonify({"error": "Raza no encontrada"}), 404

    fabrica = fabricas[raza.lower()]
    return jsonify({
        "raza": raza,
        "arma": fabrica.crear_arma().get_descripcion(),
        "armadura": fabrica.crear_armadura().get_descripcion(),
        "cuerpo": fabrica.crear_cuerpo().get_descripcion(),
        "montura": fabrica.crear_montura().get_descripcion()
    })

if __name__ == "__main__":
    app.run(debug=True)
