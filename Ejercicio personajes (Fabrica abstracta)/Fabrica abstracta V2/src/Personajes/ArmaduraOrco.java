package Personajes;

import Interfaces.IArmadura;

public class ArmaduraOrco implements IArmadura {
    @Override
    public void mostrarArmadura() {
        System.out.println("La armadura del orco es:Peto de cuero.");
    }
}