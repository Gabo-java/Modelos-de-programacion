package Personajes;

import Interfaces.ICuerpo;

public class CuerpoHumano implements ICuerpo {
    @Override
    public void mostrarCuerpo() {
        System.out.println("Cuerpo del humano:Grande y fornido.");
    }
}
