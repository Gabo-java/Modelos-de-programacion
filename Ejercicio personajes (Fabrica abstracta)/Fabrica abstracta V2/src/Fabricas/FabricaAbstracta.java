package Fabricas;

import Interfaces.IMontura;
import Interfaces.ICuerpo;
import Interfaces.IArma;
import Interfaces.IArmadura;

public abstract class FabricaAbstracta {
    public abstract IArma crearArma();
    public abstract IArmadura crearArmadura();
    public abstract IMontura crearMontura();
    public abstract ICuerpo crearCuerpo();
}