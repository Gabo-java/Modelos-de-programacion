package Personajes;

import Interfaces.ICuerpo;

public class CuerpoElfo implements ICuerpo {
    @Override
    public void mostrarCuerpo() {
        System.out.println("El cuerpo del elfo es:Mediano y Fexible.");
    }
}
