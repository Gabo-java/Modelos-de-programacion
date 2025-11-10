"""carta.py
Implementación del patrón Strategy para el comportamiento de las cartas.
Cada carta tiene una estrategia que define su efecto y acepta una potencia (valor del dado).
"""
class EstrategiaCarta:
    def aplicar(self, actor, objetivo, potencia):
        """Aplica el efecto de la carta. potencia es un entero (valor del dado usado).
        actor: instancia de Jugador que juega la carta
        objetivo: instancia de Jugador objetivo (puede ser el mismo actor en cura)
        """
        raise NotImplementedError()

    def descripcion_corta(self):
        return 'Estrategia genérica'

class AtaqueEstrategia(EstrategiaCarta):
    def aplicar(self, actor, objetivo, potencia):
        # daño directo igual a potencia
        objetivo.recibir_daño(potencia)

    def descripcion_corta(self):
        return 'Ataque: inflige daño igual al dado'

class CuraEstrategia(EstrategiaCarta):
    def aplicar(self, actor, objetivo, potencia):
        # cura al actor (potencia)
        actor.curarse(potencia)

    def descripcion_corta(self):
        return 'Cura: recupera vida igual al dado'

class DefensaEstrategia(EstrategiaCarta):
    def aplicar(self, actor, objetivo, potencia):
        # defensa: restaura salud parcial como bloqueo (potencia//2)
        actor.curarse(potencia // 2)

    def descripcion_corta(self):
        return 'Defensa: bloquea parte del daño (curación parcial)'

class Carta:
    def __init__(self, nombre, estrategia: EstrategiaCarta):
        self.nombre = nombre
        self.estrategia = estrategia

    # Nota: La aplicación con potencia se realiza llamando a estrategia.aplicar(actor, objetivo, potencia)
