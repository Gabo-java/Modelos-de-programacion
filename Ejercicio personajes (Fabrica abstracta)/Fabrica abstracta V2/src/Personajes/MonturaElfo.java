package Personajes;

import Interfaces.IMontura;

public class MonturaElfo implements IMontura {
    @Override
    public void mostrarMontura() {
        System.out.println("La montura del elfo es:Unicornio.");
    }
}
