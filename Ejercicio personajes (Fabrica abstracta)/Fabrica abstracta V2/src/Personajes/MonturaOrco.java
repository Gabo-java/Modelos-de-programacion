package Personajes;

import Interfaces.IMontura;

public class MonturaOrco implements IMontura {
    @Override
    public void mostrarMontura() {
        System.out.println("La montura del orco es:Yena giganta.");
    }
}
