package Personajes;

import Interfaces.IArmadura;

public class ArmaduraEnano implements IArmadura {
    @Override
    public void mostrarArmadura() {
        System.out.println("La armadura del enano es:Armadura de bronce.");
    }
}