package Fabricas;

import Interfaces.IArma;
import Interfaces.IArmadura;
import Interfaces.ICuerpo;
import Interfaces.IMontura;

public class FabricaControl {

    private static FabricaControl instancia;
    private FabricaAbstracta fabricaActual;

    private FabricaControl() {
    }

    public static synchronized FabricaControl getInstance() {
        if (instancia == null) {
            instancia = new FabricaControl();
        }
        return instancia;
    }

    public boolean EstableceFabrica(FabricaAbstracta fabrica) {
        if (fabricaActual != null) {
            return false;
        }
        fabricaActual = fabrica;
        return true;
    }

    public FabricaAbstracta getFabrica() {
        return fabricaActual;
    }

    public ICuerpo crearCuerpo() {
        return fabricaActual.crearCuerpo();
    }

    public IArma crearArma() {
        return fabricaActual.crearArma();
    }

    public IArmadura crearArmadura() {
        return fabricaActual.crearArmadura();
    }

    public IMontura crearMontura() {
        return fabricaActual.crearMontura();
    }
//Este es un comando de prueba que quiero mostrarle al profe para que este bien el patron de sigleton

    public void borrar() {
        fabricaActual = null;
    }
}
