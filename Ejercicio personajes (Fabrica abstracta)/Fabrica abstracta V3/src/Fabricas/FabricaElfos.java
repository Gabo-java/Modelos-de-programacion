package Fabricas;

import Personajes.ArmaduraElfo;
import Personajes.ArmaElfo;
import Personajes.CuerpoElfo;
import Personajes.MonturaElfo;
import Interfaces.IArmadura;
import Interfaces.IArma;
import Interfaces.ICuerpo;
import Interfaces.IMontura;

public class FabricaElfos extends FabricaAbstracta {

    @Override
    public IArma crearArma() {
        return new ArmaElfo();
    }

    @Override
    public IArmadura crearArmadura() {
        return new ArmaduraElfo();
    }

    @Override
    public IMontura crearMontura() {
        return new MonturaElfo();
    }

    @Override
    public ICuerpo crearCuerpo() {
        return new CuerpoElfo();
    }
}