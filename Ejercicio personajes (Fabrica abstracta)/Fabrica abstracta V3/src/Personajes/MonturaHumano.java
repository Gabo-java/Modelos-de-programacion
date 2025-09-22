package Personajes;

import Interfaces.IMontura;

public class MonturaHumano implements IMontura {
    @Override
    public void mostrarMontura() {
        System.out.println("La montura del humano es:Caballo.");
    }
}
