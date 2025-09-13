package Personajes;

import Interfaces.IArma;

public class ArmaEnano implements IArma {
    @Override
    public void mostrarArma() {
        System.out.println("El arma del enano es:Espada corta y escudo de madera.");
    }
}
