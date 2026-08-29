package org.equipo.greedy;

import org.equipo.greedy.algoritmo.SeleccionReunionesGreedy;
import org.equipo.greedy.model.Reunion;


import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
 
public class Main {
 
    public static void main(String[] args) {
 
        Scanner scanner = new Scanner(System.in);
 
        System.out.println("============================================");
        System.out.println("       PLANIFICADOR DE REUNIONES - GREEDY");
        System.out.println("============================================");
        System.out.println();
 
        // 1. Horario disponible de la sala
        System.out.print("¿Desde qué hora está disponible la sala?: ");
        int horaInicioSala = scanner.nextInt();
 
        System.out.print("¿Hasta qué hora está disponible la sala?: ");
        int horaFinSala = scanner.nextInt();
 
        // Validar horario de la sala
        while (horaInicioSala >= horaFinSala) {
 
            System.out.println();
            System.out.println(
                    "❌ El horario no es válido."
            );
            System.out.println(
                    "La hora de inicio debe ser menor que la hora final."
            );
 
            System.out.print(
                    "Ingrese nuevamente la hora de inicio: "
            );
            horaInicioSala = scanner.nextInt();
 
            System.out.print(
                    "Ingrese nuevamente la hora de finalización: "
            );
            horaFinSala = scanner.nextInt();
        }
 
        System.out.println();
        System.out.println(
                "Sala disponible: "
                        + horaInicioSala
                        + ":00 - "
                        + horaFinSala
                        + ":00"
        );
 
        // 2. Cantidad de reuniones
        System.out.println();
 
        System.out.print(
                "¿Cuántas reuniones desea ingresar?: "
        );
 
        int cantidadReuniones = scanner.nextInt();
 
        while (cantidadReuniones <= 0) {
 
            System.out.println(
                    "❌ Debe ingresar al menos una reunión."
            );
 
            System.out.print(
                    "¿Cuántas reuniones desea ingresar?: "
            );
 
            cantidadReuniones = scanner.nextInt();
        }
 
        List<Reunion> reuniones = new ArrayList<>();
 
        // 3. Ingresar reuniones
        for (int i = 1; i <= cantidadReuniones; i++) {
 
            System.out.println();
            System.out.println(
                    "----------- REUNIÓN " + i + " -----------"
            );
 
            System.out.print("Nombre: ");
            String nombre = scanner.next();
 
            System.out.print("Hora de inicio: ");
            int inicio = scanner.nextInt();
 
            System.out.print("Hora de finalización: ");
            int fin = scanner.nextInt();
 
            // Validar horario de la reunión
            if (inicio >= fin) {
 
                System.out.println();
                System.out.println(
                        "❌ La hora de inicio debe ser menor "
                                + "que la hora de finalización."
                );
 
                i--;
                continue;
            }
 
            // Validar que esté dentro del horario de la sala
            if (inicio < horaInicioSala || fin > horaFinSala) {
 
                System.out.println();
                System.out.println(
                        "❌ La reunión está fuera del horario "
                                + "disponible de la sala."
                );
 
                System.out.println(
                        "La sala está disponible de "
                                + horaInicioSala
                                + ":00 a "
                                + horaFinSala
                                + ":00."
                );
 
                i--;
                continue;
            }
 
            reuniones.add(
                    new Reunion(nombre, inicio, fin)
            );
        }
 
        // 4. Mostrar reuniones ingresadas
        System.out.println();
        System.out.println("============================================");
        System.out.println("          REUNIONES INGRESADAS");
        System.out.println("============================================");
 
        for (Reunion reunion : reuniones) {
            System.out.println(reunion);
        }
 
        // 5. Ejecutar algoritmo Greedy
        SeleccionReunionesGreedy algoritmo =
                new SeleccionReunionesGreedy();
 
        List<Reunion> resultado =
                algoritmo.seleccionar(reuniones);
 
        // 6. Mostrar resultado
        System.out.println();
        System.out.println("============================================");
        System.out.println("              RESULTADO GREEDY");
        System.out.println("============================================");
 
        System.out.println();
 
        for (Reunion reunion : resultado) {
 
            System.out.println(
                    "✓ SELECCIONADA: " + reunion
            );
        }
 
        System.out.println();
        System.out.println(
                "Total de reuniones seleccionadas: "
                        + resultado.size()
        );
 
        scanner.close();
    }
}