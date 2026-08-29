# Analisis-Algoritmos
# Planificador de Reuniones - Algoritmo Greedy

## Descripción del proyecto

Este proyecto implementa un **algoritmo Greedy (voraz)** para seleccionar la mayor cantidad posible de reuniones que puedan realizarse en una misma sala sin que sus horarios se superpongan.

El programa funciona mediante la consola y permite al usuario indicar el horario disponible de la sala, ingresar diferentes reuniones con su nombre, hora de inicio y hora de finalización, y finalmente obtener un conjunto de reuniones seleccionadas por el algoritmo Greedy.

El objetivo principal es aplicar el concepto de **selección de actividades**, donde se busca seleccionar la mayor cantidad de reuniones compatibles entre sí.

---

## ¿Cómo funciona?

El programa sigue los siguientes pasos:

1. El usuario indica la hora de inicio y finalización de disponibilidad de la sala.
2. El programa valida que el horario de la sala sea correcto.
3. El usuario indica cuántas reuniones desea ingresar.
4. Para cada reunión se solicita:

   * Nombre.
   * Hora de inicio.
   * Hora de finalización.
5. El programa valida que:

   * La hora de inicio sea menor que la hora de finalización.
   * La reunión se encuentre dentro del horario disponible de la sala.
6. Las reuniones ingresadas se procesan mediante el algoritmo Greedy.
7. El algoritmo ordena las reuniones según su hora de finalización.
8. Se seleccionan las reuniones compatibles, comenzando por las que terminan más temprano.
9. Finalmente, el programa muestra las reuniones seleccionadas y la cantidad total.

---

## Algoritmo Greedy utilizado

La clase `SeleccionReunionesGreedy` implementa la estrategia Greedy para el problema de selección de reuniones.

La estrategia consiste en:

* Ordenar todas las reuniones de acuerdo con su hora de finalización.
* Seleccionar la primera reunión que sea compatible.
* Continuar seleccionando reuniones cuya hora de inicio sea mayor o igual a la hora de finalización de la última reunión seleccionada.

La decisión Greedy utilizada es **elegir siempre la reunión que termina más temprano**, porque esto deja disponible la mayor cantidad de tiempo posible para seleccionar otras reuniones posteriormente.

### Ejemplo

Si se tienen las siguientes reuniones:

```text
Reunión A: 8:00 - 10:00
Reunión B: 9:00 - 11:00
Reunión C: 10:00 - 12:00
Reunión D: 11:00 - 13:00
```

El algoritmo puede seleccionar:

```text
Reunión A: 8:00 - 10:00
Reunión C: 10:00 - 12:00
```

Estas reuniones no se superponen y permiten aprovechar el horario disponible.

---

## Estructura del proyecto

El proyecto se encuentra organizado en diferentes paquetes, separando la lógica principal del algoritmo, el modelo de datos y la ejecución del programa.


**`Main.java`**

Es la clase principal del programa. Se encarga de interactuar con el usuario mediante la consola.

Sus principales funciones son:

* Solicitar el horario disponible de la sala.
* Validar el horario de la sala.
* Solicitar la cantidad de reuniones.
* Registrar las reuniones.
* Validar los horarios ingresados.
* Ejecutar el algoritmo Greedy.
* Mostrar las reuniones seleccionadas.

---

---

## Flujo general del programa

```text
Inicio
   ↓
Ingresar horario disponible de la sala
   ↓
Validar horario
   ↓
Ingresar cantidad de reuniones
   ↓
Ingresar nombre, inicio y fin de cada reunión
   ↓
Validar reuniones
   ↓
Mostrar reuniones ingresadas
   ↓
Ordenar reuniones por hora de finalización
   ↓
Aplicar algoritmo Greedy
   ↓
Seleccionar reuniones compatibles
   ↓
Mostrar resultado
   ↓
Fin
```

---

## Tecnologías utilizadas

* **Java**
* Programación orientada a objetos
* Algoritmo Greedy
* Entrada de datos mediante `Scanner`
* Colecciones mediante `List` y `ArrayList`
* Ordenamiento mediante `Comparator`

---

## Objetivo académico

El proyecto tiene como finalidad demostrar la aplicación práctica de un algoritmo Greedy para resolver un problema de planificación de actividades.

A través del planificador de reuniones se evidencia cómo una estrategia de selección local puede utilizarse para construir una solución eficiente al problema de seleccionar el mayor número posible de reuniones sin conflictos de horario.

---

## Integrantes

* ALEJANDRA CARVAJAL CAMPO
* JOSUE ACOSTA LONDOÑO
* ARGENIS ALEJANDRO RUIZ COTES 

