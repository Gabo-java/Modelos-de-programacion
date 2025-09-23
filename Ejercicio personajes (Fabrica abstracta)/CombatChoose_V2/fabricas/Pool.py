from fabricas.fabrica_humanos import FabricaHumanos
from fabricas.fabrica_elfos import FabricaElfos
from fabricas.fabrica_orcos import FabricaOrcos
from fabricas.fabrica_enanos import FabricaEnanos
import random
import os

class Pool:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Pool, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'fabricas'):
            self.fabricas = {
                "elfo": FabricaElfos(),
                "humano": FabricaHumanos(),
                "enano": FabricaEnanos(),
                "orco": FabricaOrcos()
            }
            self.personajes_creados = {}

    def get_fabrica(self, raza):
        return self.fabricas.get(raza)

    def get_personaje(self, raza):
        if raza not in self.personajes_creados:
            fabrica = self.get_fabrica(raza)
            if fabrica:

                def get_random_image(componente, race):
                    base_name = f"{componente}_{race}"
                    if componente == "cuerpo":
                        base_name = race
                    
                    img_folder = os.path.join(os.path.dirname(__file__), '..', 'static', 'img')
                    
                    possible_images = [
                        f for f in os.listdir(img_folder) 
                        if f.startswith(base_name) and (f.endswith('.png') or f.endswith('.jpg'))
                    ]
                    
                    if not possible_images:
                        # Fallback a la imagen por defecto si no se encuentra ninguna
                        return f"{base_name}.png"
                        
                    return random.choice(possible_images)

                self.personajes_creados[raza] = {
                    "arma": {"obj": fabrica.crear_arma(), "img": get_random_image("arma", raza)},
                    "armadura": {"obj": fabrica.crear_armadura(), "img": get_random_image("armadura", raza)},
                    "cuerpo": {"obj": fabrica.crear_cuerpo(), "img": get_random_image("cuerpo", raza)},
                    "montura": {"obj": fabrica.crear_montura(), "img": get_random_image("montura", raza)}
                }
        return self.personajes_creados.get(raza)
