package org.equipo.greedy.model;

public class Reunion {

    private String nombre;
    private int inicio;
    private int fin;

    public Reunion(String nombre, int inicio, int fin) {
        this.nombre = nombre;
        this.inicio = inicio;
        this.fin = fin;
    }

    public String getNombre() {
        return nombre;
    }

    public int getInicio() {
        return inicio;
    }

    public int getFin() {
        return fin;
    }

    @Override
    public String toString() {
        return nombre + " (" + inicio + ":00 - " + fin + ":00)";
    }
}
