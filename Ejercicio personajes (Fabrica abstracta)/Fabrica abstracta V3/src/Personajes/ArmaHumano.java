package Personajes;

import Interfaces.IArma;

public class ArmaHumano implements IArma {
    @Override
    public void mostrarArma() {
        System.out.println("El arma del humano es:Lanza.");
    }
}
