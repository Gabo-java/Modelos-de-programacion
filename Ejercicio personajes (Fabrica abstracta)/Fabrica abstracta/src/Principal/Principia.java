package Principal;
import Interfaces.IArmadura;
import Interfaces.IArma;
import Interfaces.ICuerpo;
import Interfaces.IMontura;
import Fabricas.FabricaAbstracta;
import java.util.Scanner;
public class Principia {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Bienvenidos al MMORPG me quedo dormido v0.1");
        System.out.println("Porfavor elige una raza");
        System.out.println("1)Humano");
        System.out.print("Seleccione una opcion:");

        int opcion = sc.nextInt();
        FabricaAbstracta fabrica = null;

        if (opcion == 1) {
            fabrica = new Fabricas.FabricaHumanos();
        } else {
            System.out.println("Esa opcion no esta disponible.");
            System.exit(0);
        }

        System.out.println("\nCreando tu personaje...\n");

        ICuerpo cuerpo = fabrica.crearCuerpo();
        IArma arma = fabrica.crearArma();
        IArmadura armadura = fabrica.crearArmadura();
        IMontura montura = fabrica.crearMontura();

        cuerpo.mostrarCuerpo();
        arma.mostrarArma();
        armadura.mostrarArmadura();
        montura.mostrarMontura();
        
        System.out.println("Le informamos que en la v0.2 se agregara la expacion de la sagrada arbolera con la nueva raza de los elfos");

        sc.close();
    }
}