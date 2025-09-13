package Personajes;

import Interfaces.ICuerpo;

public class CuerpoHumano implements ICuerpo {
    @Override
    public void mostrarCuerpo() {
        System.out.println("El cuerpo del humano es:Grande y fornido.");
    }
}
