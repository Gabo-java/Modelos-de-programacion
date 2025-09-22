package Personajes;

import Interfaces.IMontura;

public class MonturaEnano implements IMontura {
    @Override
    public void mostrarMontura() {
        System.out.println("La montura del enano es:Cabra.");
    }
}
