package Personajes;

import Interfaces.IArmadura;

public class ArmaduraElfo implements IArmadura {
    @Override
    public void mostrarArmadura() {
        System.out.println("La armadura del elfo es:Tunica.");
    }
}