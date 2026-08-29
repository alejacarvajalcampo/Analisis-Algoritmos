package org.equipo.greedy;

import org.equipo.greedy.algoritmo.SeleccionReunionesGreedy;
import org.equipo.greedy.model.Reunion;

import java.util.ArrayList;
import java.util.List;

public class Main {

    public static void main(String[] args) {

        List<Reunion> reuniones = new ArrayList<>();

        reuniones.add(new Reunion("A", 9, 10));
        reuniones.add(new Reunion("B", 9, 11));
        reuniones.add(new Reunion("C", 10, 11));
        reuniones.add(new Reunion("D", 11, 12));
        reuniones.add(new Reunion("E", 11, 13));
        reuniones.add(new Reunion("F", 12, 13));
        reuniones.add(new Reunion("G", 13, 14));

        SeleccionReunionesGreedy algoritmo =
                new SeleccionReunionesGreedy();

        List<Reunion> resultado =
                algoritmo.seleccionar(reuniones);

        System.out.println("Reuniones seleccionadas:");

        for (Reunion reunion : resultado) {
            System.out.println(reunion);
        }

        System.out.println(
                "Total: " + resultado.size()
        );
    }
}