package org.equipo.greedy.algoritmo;


import org.equipo.greedy.model.Reunion;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
public class SeleccionReunionesGreedy {

    public List<Reunion> seleccionar(
            List<Reunion> reuniones) {

        reuniones.sort(
                Comparator.comparingInt(Reunion::getFin)
        );

        List<Reunion> seleccionadas =
                new ArrayList<>();

        int ultimaHoraFin = 0;

        System.out.println();
        System.out.println(
                "============================================"
        );
        System.out.println(
                "          EJECUCIÓN DEL ALGORITMO"
        );
        System.out.println(
                "============================================"
        );

        System.out.println();
        System.out.println(
                "Reuniones ordenadas por hora de finalización:"
        );

        for (Reunion reunion : reuniones) {
            System.out.println(reunion);
        }

        System.out.println();
        System.out.println("Evaluando reuniones...");
        System.out.println();

        for (Reunion reunion : reuniones) {

            if (reunion.getInicio() >= ultimaHoraFin) {

                seleccionadas.add(reunion);

                ultimaHoraFin = reunion.getFin();

                System.out.println(
                        reunion.getNombre()
                                + " → ✓ SELECCIONADA"
                );

            } else {

                System.out.println(
                        reunion.getNombre()
                                + " → ✗ DESCARTADA"
                                + " (se superpone)"
                );
            }
        }

        return seleccionadas;
    }
}
