"""carta.py
Patrones Strategy para cartas: Ataque, Cura, Defensa, Objetos.
"""
from configuracion import ESTILOS_CARTAS

class EstrategiaCarta:
    def aplicar(self, actor, objetivo, potencia: int, contexto: dict | None = None):
        raise NotImplementedError

    def descripcion_corta(self) -> str:
        return "Estrategia genérica"

class EstrategiaAtaque(EstrategiaCarta):
    def aplicar(self, actor, objetivo, potencia: int, contexto=None):
        daño_base = potencia + actor.bono_ataque_turno
        objetivo.recibir_daño(daño_base)

    def descripcion_corta(self) -> str:
        return "Ataque directo usando el valor del dado."

class EstrategiaCura(EstrategiaCarta):
    def aplicar(self, actor, objetivo, potencia: int, contexto=None):
        actor.curarse(potencia)

    def descripcion_corta(self) -> str:
        return "Cura tu vida según el valor del dado."

class EstrategiaDefensa(EstrategiaCarta):
    def aplicar(self, actor, objetivo, potencia: int, contexto=None):
        puntos_escudo = 1 + potencia
        actor.agregar_escudo(puntos_escudo)

    def descripcion_corta(self) -> str:
        return "Escudo 1 turno (1 + dado)."

class EstrategiaObjetos(EstrategiaCarta):
    """Usa ObjectPool + Fábrica para generar y aplicar un objeto."""

    def aplicar(self, actor, objetivo, potencia: int, contexto=None):
        if contexto is None:
            return
        pool_objetos = contexto.get("pool_objetos")
        if actor.objeto_usado_en_turno:
            return

        if potencia <= 2:
            calidad = "baja"
        elif potencia <= 4:
            calidad = "media"
        else:
            calidad = "alta"

        objeto = pool_objetos.obtener_objeto_aleatorio(calidad)
        if objeto is None:
            return

        objeto.aplicar(actor, objetivo, contexto)
        actor.objeto_usado_en_turno = True
        pool_objetos.devolver_objeto(objeto)
        contexto["mensaje"] = f"{actor.nombre} usó objeto: {objeto.nombre}"

class Carta:
    def __init__(self, nombre: str, tipo: str, estrategia: EstrategiaCarta):
        self.nombre = nombre
        self.tipo = tipo  # "ataque", "cura", "defensa", "objetos"
        self.estrategia = estrategia
        self.usada_en_turno = False

    def resetear_turno(self):
        self.usada_en_turno = False

    def puede_usarse(self, jugador) -> bool:
        if self.usada_en_turno:
            return False
        if self.tipo == "objetos" and jugador.objeto_usado_en_turno:
            return False
        return True

    def estilos(self):
        return ESTILOS_CARTAS.get(self.tipo, ESTILOS_CARTAS["ataque"])
