"""object_pool.py
Object Pool para reutilizar instancias de objetos.
"""

import random


class ObjectPoolObjetos:
    def __init__(self, fabrica):
        self.fabrica = fabrica
        self.pool_por_tipo: dict[str, list] = {}

        self.tipos_por_calidad = {
            "baja": ["aumento_ataque", "aumento_defensa", "bandita"],
            "media": ["dados_plata", "piromancia", "pergamino_proteccion"],
            "alta": ["dados_oro", "dado_fantasma", "defensa_absoluta"],
        }

    def _obtener_desde_pool(self, tipo: str):
        lista = self.pool_por_tipo.setdefault(tipo, [])
        if lista:
            return lista.pop()
        return self.fabrica.crear_objeto(tipo)

    def obtener_objeto_aleatorio(self, calidad: str):
        tipos = self.tipos_por_calidad.get(calidad)
        if not tipos:
            return None
        tipo_elegido = random.choice(tipos)
        return self._obtener_desde_pool(tipo_elegido)

    def devolver_objeto(self, objeto):
        objeto.resetear()
        nombre_clase = objeto.__class__.__name__
        mapa_inverso = {
            "ObjetoAumentoAtaque": "aumento_ataque",
            "ObjetoAumentoDefensa": "aumento_defensa",
            "ObjetoBandita": "bandita",
            "ObjetoDadosPlata": "dados_plata",
            "ObjetoPiromancia": "piromancia",
            "ObjetoPergaminoProteccion": "pergamino_proteccion",
            "ObjetoDadosOro": "dados_oro",
            "ObjetoDadoFantasma": "dado_fantasma",
            "ObjetoDefensaAbsoluta": "defensa_absoluta",
        }
        tipo = mapa_inverso.get(nombre_clase)
        if tipo is None:
            return
        lista = self.pool_por_tipo.setdefault(tipo, [])
        lista.append(objeto)
