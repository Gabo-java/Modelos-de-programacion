package Personajes;

import Interfaces.ICuerpo;

public class CuerpoOrco implements ICuerpo {
    @Override
    public void mostrarCuerpo() {
        System.out.println("El cuerpo del orco es:Muy grande y fuerte.");
    }
}
