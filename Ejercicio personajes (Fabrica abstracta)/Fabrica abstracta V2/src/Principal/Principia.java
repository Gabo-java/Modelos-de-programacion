package Principal;

import Interfaces.IArmadura;
import Interfaces.IArma;
import Interfaces.ICuerpo;
import Interfaces.IMontura;
import Fabricas.FabricaAbstracta;
import java.util.Scanner;

public class Principia {

    public static void main(String[] args) {
        Scanner opc = new Scanner(System.in);

        System.out.println("Bienvenidos al MMORPG me quedo dormido Close beta");

        FabricaAbstracta fabrica = null;
        int opcion = 0;
        boolean valido = false;
        
        while (!valido) {
            System.out.println("Por favor elige una raza");
            System.out.println("1)Humano.");
            System.out.println("2)Elfo.");
            System.out.println("3)Orco.");
            System.out.println("4)Enano.");
            System.out.print("Seleccione una opcion:");

            opcion = opc.nextInt();

            switch (opcion) {
                case 1 -> {
                    fabrica = new Fabricas.FabricaHumanos();
                    System.out.println("El humano es el habitante mas comun de esta tierras no destaca en nada pero tampoco es malo en algo");
                    System.out.println("El humano no puede llegar al nivel 10 de magias y armas");
                    System.out.println("Habilidad pasiva (Ambicion):Aumenta la expericia en armas y magias en un 30% este efecto se triplica en niveles 1 a 3 ademas puedes equipar 6 habilidades de nivel 9");
                }
                case 2 -> {
                    fabrica = new Fabricas.FabricaElfos();
                    System.out.println("Viviendo en la arbolada los elfos son los mejores usuarios de magia debido a la longevidad de su especie");
                    System.out.println("Habilidad pasiva (Sabio del bosque):Las primeras tres habilidades equipas reducen el costo de mana en un 15%");
                }
                case 3 -> {
                    fabrica = new Fabricas.FabricaOrcos();
                    System.out.println("Los orcos son formidos guerreros que se dedican a vagar por las tierra ofreciendo su fuerza por un buen precio");
                    System.out.println("Habilidad pasiva (indomito):Aumenta la fuerza en 10 puntos ademas si tu salud esta por debajo del 50% por cada bloque perfecto o parry que hagas te curas un 2.5% de la vida maxima");
                }
                case 4 -> {
                    fabrica = new Fabricas.FabricaEnanos();
                    System.out.println("Con una gran resistencia y habilidades para la herreria los enanos son reconocidos por todo el mundo");
                    System.out.println("Habilidad pasiva (Barba de hierro):Ganas 25 puntos de defensa magica y fisica ademas estas defensas aunmenta 5 puntos extra por cada enemigo que te este atacan hasta un maximo de 5");
                }
                default -> {
                    System.out.println("Esa opcion no esta disponible intenta de nuevo");
                    continue;
                }
            }
            System.out.print("Desea confirmar la creacion del personaje con esta raza (Si=1 No=2):");
            int confirmacion = opc.nextInt();
            if (confirmacion == 1) {
                valido = true;
            } else {
            }
        }

        System.out.println("Creando tu personaje");

        ICuerpo cuerpo = fabrica.crearCuerpo();
        IArma arma = fabrica.crearArma();
        IArmadura armadura = fabrica.crearArmadura();
        IMontura montura = fabrica.crearMontura();

        cuerpo.mostrarCuerpo();
        arma.mostrarArma();
        armadura.mostrarArmadura();
        montura.mostrarMontura();

        System.out.println("Le solicitamos que nos informe de cualquier bug o error que se presente en su sesion y bienvenido.");
    }
}

