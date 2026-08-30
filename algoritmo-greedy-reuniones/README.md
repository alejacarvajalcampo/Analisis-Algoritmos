# Algoritmo Greedy - Selección de Reuniones

Proyecto académico para la asignatura Análisis de Algoritmos.

## Problema

Seleccionar el mayor número posible de reuniones que puedan
realizarse en una única sala sin superposición.

## Algoritmo

Se utilizará un algoritmo Greedy basado en seleccionar
la reunión compatible que termine más temprano.

## Tecnologías

- Java
- Gradle
- IntelliJ IDEA
- Git
- GitHub

# Problema

Una empresa dispone de una única sala de reuniones y tiene
varias reuniones programadas durante el día.

Cada reunión posee una hora de inicio y una hora de finalización.

Debido a que existe una única sala, dos reuniones no pueden
realizarse simultáneamente.

## Objetivo

Seleccionar el mayor número posible de reuniones sin
superposición.

# Algoritmo Greedy

## Estrategia

El algoritmo ordena las reuniones por su hora de finalización.

Posteriormente recorre las reuniones y selecciona aquellas cuya
hora de inicio sea mayor o igual a la hora de finalización de la
última reunión seleccionada.

## Criterio Greedy

En cada paso se selecciona la reunión compatible que termina
más temprano.

## Resultado

Para el ejemplo utilizado se obtiene:

A → C → E → G

Total:

4 reuniones.
