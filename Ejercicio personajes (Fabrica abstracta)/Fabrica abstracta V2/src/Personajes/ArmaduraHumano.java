package Personajes;

import Interfaces.IArmadura;

public class ArmaduraHumano implements IArmadura {
    @Override
    public void mostrarArmadura() {
        System.out.println("La armadura del humano es:Cota de malla.");
    }
}