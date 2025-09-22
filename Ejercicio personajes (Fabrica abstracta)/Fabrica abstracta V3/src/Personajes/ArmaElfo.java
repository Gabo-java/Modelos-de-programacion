package Personajes;

import Interfaces.IArma;

public class ArmaElfo implements IArma {
    @Override
    public void mostrarArma() {
        System.out.println("El arma del elfo es:Baston.");
    }
}
