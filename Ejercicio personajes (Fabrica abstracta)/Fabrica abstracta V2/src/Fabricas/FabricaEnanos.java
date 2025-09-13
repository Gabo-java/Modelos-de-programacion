package Fabricas;

import Personajes.ArmaduraEnano;
import Personajes.ArmaEnano;
import Personajes.CuerpoEnano;
import Personajes.MonturaEnano;
import Interfaces.IArmadura;
import Interfaces.IArma;
import Interfaces.ICuerpo;
import Interfaces.IMontura;

public class FabricaEnanos extends FabricaAbstracta {

    @Override
    public IArma crearArma() {
        return new ArmaEnano();
    }

    @Override
    public IArmadura crearArmadura() {
        return new ArmaduraEnano();
    }

    @Override
    public IMontura crearMontura() {
        return new MonturaEnano();
    }

    @Override
    public ICuerpo crearCuerpo() {
        return new CuerpoEnano();
    }
}