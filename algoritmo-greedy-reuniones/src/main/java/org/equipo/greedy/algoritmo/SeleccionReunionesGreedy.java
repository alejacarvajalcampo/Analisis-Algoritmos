package org.equipo.greedy.algoritmo;


import org.equipo.greedy.model.Reunion;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
public class SeleccionReunionesGreedy {

    public List<Reunion> seleccionar(List<Reunion> reuniones) {

        reuniones.sort(Comparator.comparingInt(Reunion::getFin));

        List<Reunion> seleccionadas = new ArrayList<>();

        int ultimaHoraFin = 0;

        for (Reunion reunion : reuniones) {

            if (reunion.getInicio() >= ultimaHoraFin) {
                seleccionadas.add(reunion);
                ultimaHoraFin = reunion.getFin();
            }
        }

        return seleccionadas;
    }
}