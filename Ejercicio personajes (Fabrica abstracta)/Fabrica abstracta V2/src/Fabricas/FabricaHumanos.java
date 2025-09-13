package Fabricas;

import Personajes.ArmaduraHumano;
import Personajes.ArmaHumano;
import Personajes.CuerpoHumano;
import Personajes.MonturaHumano;
import Interfaces.IArmadura;
import Interfaces.IArma;
import Interfaces.ICuerpo;
import Interfaces.IMontura;

public class FabricaHumanos extends FabricaAbstracta {

    @Override
    public IArma crearArma() {
        return new ArmaHumano();
    }

    @Override
    public IArmadura crearArmadura() {
        return new ArmaduraHumano();
    }

    @Override
    public IMontura crearMontura() {
        return new MonturaHumano();
    }

    @Override
    public ICuerpo crearCuerpo() {
        return new CuerpoHumano();
    }
}