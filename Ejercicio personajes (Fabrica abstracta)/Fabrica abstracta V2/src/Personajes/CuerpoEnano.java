package Personajes;

import Interfaces.ICuerpo;

public class CuerpoEnano implements ICuerpo {
    @Override
    public void mostrarCuerpo() {
        System.out.println("El cuerpo del enano es:Chiquito y resistente.");
    }
}
