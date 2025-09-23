from flask import Flask, render_template, jsonify
from fabricas.Pool import Pool
from fabricas.fabrica_humanos import FabricaHumanos
from fabricas.fabrica_elfos import FabricaElfos
from fabricas.fabrica_orcos import FabricaOrcos
from fabricas.fabrica_enanos import FabricaEnanos

app = Flask(__name__)
pool = Pool()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/seleccionar/<raza>")
def seleccionar_raza(raza):
    personaje = pool.get_personaje(raza.lower())

    if not personaje:
        return render_template("seleccion.html", error="Raza no encontrada")

    datos = {
        "raza": raza.capitalize(),
        "arma": {
            "desc": personaje["arma"]["obj"].get_descripcion(),
            "img": personaje["arma"]["img"]
        },
        "armadura": {
            "desc": personaje["armadura"]["obj"].get_descripcion(),
            "img": personaje["armadura"]["img"]
        },
        "cuerpo": {
            "desc": personaje["cuerpo"]["obj"].get_descripcion(),
            "img": personaje["cuerpo"]["img"]
        },
        "montura": {
            "desc": personaje["montura"]["obj"].get_descripcion(),
            "img": personaje["montura"]["img"]
        }
    }

    return render_template("seleccion.html", datos=datos)


@app.route("/api/seleccionar/<raza>")
def api_seleccionar_raza(raza):
    personaje = pool.get_personaje(raza.lower())

    if not personaje:
        return jsonify({"error": "Raza no encontrada"}), 404

    return jsonify({
        "raza": raza,
        "arma": personaje["arma"]["obj"].get_descripcion(),
        "armadura": personaje["armadura"]["obj"].get_descripcion(),
        "cuerpo": personaje["cuerpo"]["obj"].get_descripcion(),
        "montura": personaje["montura"]["obj"].get_descripcion()
    })

if __name__ == "__main__":
    app.run(debug=True)
