# Optimización de Pipeline CI/CD con Programación Dinámica

Este repositorio contiene la entrega correspondiente al Examen 3 de Análisis de Algoritmos. Se seleccionó la *Opción 1 (Desarrollo)*. El proyecto implementa una API REST en Python utilizando Flask, separando la lógica matemática del enrutamiento web.

## El problema planteado
En entornos de despliegue continuo (CI/CD), el tiempo de paso a producción suele ser crítico. Ante un despliegue de emergencia (hotfix), es imposible ejecutar toda la suite de pruebas de software (SQA) sin exceder la ventana de mantenimiento. 

El problema consiste en determinar qué conjunto exacto de pruebas automatizadas (unitarias, análisis estático de código, E2E, auditoría de seguridad) se debe ejecutar para maximizar la mitigación de riesgos (valor), sin superar el tiempo máximo disponible (capacidad).

## Algoritmo seleccionado
Se implementó una variación del *Problema de la Mochila 0/1 (0/1 Knapsack Problem)*, resuelto mediante el enfoque de tabulación (Bottom-Up) de Programación Dinámica.

## Análisis del Algoritmo

### 1. Definición del estado y subproblemas
Se construyó una matriz bidimensional llamada dp. 
El estado dp[i][w] representa el valor máximo de mitigación de riesgo que se puede obtener evaluando un subconjunto de las primeras i herramientas de prueba, disponiendo de un límite de tiempo de w minutos.

### 2. Relación de recurrencia
Al evaluar la herramienta i (con un costo de tiempo t y un valor de mitigación v), el algoritmo toma una decisión binaria:
*   Si el tiempo de la herramienta excede el límite evaluado (t > w), no se puede incluir y se hereda el estado anterior: 
    dp[i][w] = dp[i-1][w]
*   Si la herramienta cabe en el tiempo (t <= w), se elige el máximo entre no incluirla o incluirla (sumando su valor y restando su tiempo del límite actual):
    dp[i][w] = max(dp[i-1][w], dp[i-1][w-t] + v)

### 3. Casos base
Si la capacidad de tiempo es 0 (w = 0) o si no se evalúa ninguna herramienta (i = 0), el valor máximo de mitigación es 0. En la implementación de Python, esto se maneja de forma implícita inicializando la matriz completa con ceros antes de ejecutar los ciclos anidados.

## Arquitectura y Ejecución
Se aplicó el principio de separación de responsabilidades:
*   optimizer.py: Contiene exclusivamente el motor matemático y la matriz del algoritmo.
*   app.py: Maneja la validación de los datos JSON y expone el algoritmo mediante un endpoint POST HTTP.

### Instrucciones de despliegue local
1. Crear el entorno virtual: python -m venv venv
2. Activar el entorno e instalar dependencias: pip install -r requirements.txt
3. Levantar el servidor: python app.py
4. Enviar un payload JSON mediante POST a http://localhost:5000/api/optimizar con la estructura: {"tiempo_limite": 10}

## Video de Sustentación
*Enlace al video:*