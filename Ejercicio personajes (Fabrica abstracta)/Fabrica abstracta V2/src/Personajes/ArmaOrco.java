package Personajes;

import Interfaces.IArma;

public class ArmaOrco implements IArma {
    @Override
    public void mostrarArma() {
        System.out.println("El arma del orco es:Porra con pinchos.");
    }
}
