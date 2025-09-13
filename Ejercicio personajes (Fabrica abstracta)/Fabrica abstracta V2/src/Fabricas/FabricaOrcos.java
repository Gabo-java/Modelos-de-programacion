package Fabricas;

import Personajes.ArmaduraOrco;
import Personajes.ArmaOrco;
import Personajes.CuerpoOrco;
import Personajes.MonturaOrco;
import Interfaces.IArmadura;
import Interfaces.IArma;
import Interfaces.ICuerpo;
import Interfaces.IMontura;

public class FabricaOrcos extends FabricaAbstracta {

    @Override
    public IArma crearArma() {
        return new ArmaOrco();
    }

    @Override
    public IArmadura crearArmadura() {
        return new ArmaduraOrco();
    }

    @Override
    public IMontura crearMontura() {
        return new MonturaOrco();
    }

    @Override
    public ICuerpo crearCuerpo() {
        return new CuerpoOrco();
    }
}