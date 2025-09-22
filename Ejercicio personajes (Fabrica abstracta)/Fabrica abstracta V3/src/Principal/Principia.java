package Principal;

import Interfaces.IArmadura;
import Interfaces.IArma;
import Interfaces.ICuerpo;
import Interfaces.IMontura;
import Fabricas.FabricaAbstracta;
import Fabricas.FabricaControl;
import java.util.Scanner;

public class Principia {

    public static void main(String[] args) {
        Scanner opc = new Scanner(System.in);

        System.out.println("Bienvenidos al RPG me quedo dormido Close beta 2");

        FabricaAbstracta fabrica = null;
        FabricaControl control = FabricaControl.getInstance();
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
                    System.out.println("Humanos");
                    System.out.println("Una raza de guerreros formidable ubicados en el norte del continente de Solista bastante diestros en el combate a media distancia.");
                    System.out.println("Habilidad pasiva (Ambicion):Ganas 25% de experiencia y oro");
                    System.out.println("Dificultada:Media");
                    System.out.println("Estadisticas:Vida=40/Mana=25/Ataque=30/Velocidad=25/Defensa=5");
                }
                case 2 -> {
                    fabrica = new Fabricas.FabricaElfos();
                    System.out.println("Elfos");
                    System.out.println("Una raza increiblemente longeva gracias a esa longevidad les ha permitido perfeccionar cada tipo de magia");
                    System.out.println("Habilidad pasiva (Sabio del bosque):Reduce el consumo de mana de la primera habilidad en un 20%");
                    System.out.println("Habilidad activa (Magia arcana):Aumenta la potencia de tu hechizo en un 250% o lo aumenta su potencia en 130% y pasa a ser daño verdadero (cd 3 turnos)");
                    System.out.println("Dificultad:Media/Alta");
                    System.out.println("Tipo:Mago");
                    System.out.println("Estadisticas:Vida=35/Mana=40/Magia=30/Velocidad=18/Defensa=2");
                }
                case 3 -> {
                    fabrica = new Fabricas.FabricaOrcos();
                    System.out.println("Orcos");
                    System.out.println("Una raza increiblemente fuerte pero muy susceptible a sus emociones.");
                    System.out.println("Habilidad pasiva (Colera):Aumentas tu daño en 2 puntos por cada 10% de tu vida maxima perdida hasta un maximo de 10.");
                    System.out.println("Habilidad activa (Berserk):Pierdes un 50% de tu vida maxima y ganas un 90% de esa vida como escudo si tienes menos de 50% de tu vida maxima pasa a ser Inquebrantable (cd 2 Turnos).");
                    System.out.println("Inquebrantable:te da robo de vida de un 10% del daño infligido durante 2 turnos");
                    System.out.println("Dificultad:Dificil");
                    System.out.println("TIpo:Berserk");
                    System.out.println("Estadisticas:Vida=45/Mana=15/Ataque=37/Velocidad=28/Defensa=0");
                }
                case 4 -> {
                    System.out.println("Enanos");
                    System.out.println("Una raza reconocida por su gran habilidad en la herreria, pero tambien su alta resistencia y tolerancia al dolor.");
                    System.out.println("Habilidad pasiva (barba de hierro):Ganas un pequeño escudo que escala con tu armadura cada 2 turnos.");
                    System.out.println("Habilidad activa (Explosion):Pierdes un 50% de tu escudo actual y lo conviertes en daño (cd 2 turnos).");
                    System.out.println("Dificultad:Facil");
                    System.out.println("Tipo:Tanque");
                    System.out.println("Estadisticas:Vida=50/Mana=20/Ataque=20/Velocidad=15/Defensa=20");
                }
                default -> {
                    System.out.println("Esa opcion no esta disponible intenta de nuevo");
                    continue;
                }
            }

            System.out.print("Desea confirmar la creacion del personaje con esta raza (Si=1 No=2):");
            int confirmacion = opc.nextInt();
            if (confirmacion == 1) {
                control.EstableceFabrica(fabrica);
                valido = true;
            } else {
                System.out.println("Esa opcion no esta disponible");
            }
        }

        System.out.println("Creando tu personaje");

        ICuerpo cuerpo = control.crearCuerpo();
        IArma arma = control.crearArma();

        //control.borrar();
        //fabrica = new Fabricas.FabricaEnanos();
        //control.EstableceFabrica(fabrica);
        
        IArmadura armadura = control.crearArmadura();
        IMontura montura = control.crearMontura();

        cuerpo.mostrarCuerpo();
        arma.mostrarArma();
        armadura.mostrarArmadura();
        montura.mostrarMontura();

        System.out.println("Le solicitamos que nos informe de cualquier bug o error que se presente en su sesion y bienvenido.");
    }
}
