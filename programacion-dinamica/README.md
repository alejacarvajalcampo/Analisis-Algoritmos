# Optimización de Pipeline CI/CD con Programación Dinámica

Este repositorio contiene la entrega correspondiente al Examen 3 de Análisis de Algoritmos, aplicando la *Opción 1 (Desarrollo)*[cite: 1]. 

El proyecto consiste en una aplicación de escritorio nativa construida en Python (Tkinter), estructurada bajo el principio de separación de responsabilidades: la lógica matemática del algoritmo está completamente aislada de la interfaz gráfica de usuario (GUI).

## El Problema Planteado
En entornos de despliegue continuo (CI/CD), el tiempo de paso a producción es una métrica crítica. Ante un despliegue de emergencia (hotfix), es imposible ejecutar toda la suite de pruebas de software (SQA) sin exceder la ventana de mantenimiento[cite: 1]. 

El problema a solucionar consiste en determinar qué conjunto exacto de pruebas automatizadas (unitarias, análisis estático, E2E, auditoría de seguridad) se debe ejecutar para *maximizar la mitigación de riesgos (valor), sin superar el **tiempo máximo disponible (capacidad)*[cite: 1].

## Algoritmo Seleccionado
Se implementó el algoritmo clásico del *Problema de la Mochila 0/1 (0/1 Knapsack Problem)*, utilizando el enfoque de tabulación (Bottom-Up) de Programación Dinámica[cite: 1].

### 1. Definición del estado y subproblemas
Se construyó una matriz bidimensional llamada dp[cite: 1]. 
El estado dp[i][w] representa el valor máximo de mitigación de riesgo que se puede obtener evaluando un subconjunto de las primeras i herramientas de prueba, disponiendo de un límite de tiempo de w minutos[cite: 1].

### 2. Relación de recurrencia
Al iterar sobre los subproblemas y evaluar la herramienta i (con un costo de tiempo t y un valor de mitigación v), el algoritmo toma una decisión óptima[cite: 1, 2]:
*   Si el tiempo de la herramienta excede el límite evaluado (t > w), no se puede incluir y se hereda el estado óptimo anterior: 
    dp[i][w] = dp[i-1][w]
*   Si la herramienta cabe en el tiempo (t <= w), se elige el máximo entre no incluirla o incluirla (sumando su valor y restando su tiempo del límite actual):
    dp[i][w] = max(dp[i-1][w], dp[i-1][w-t] + v)

### 3. Manejo de casos base
Si la capacidad de tiempo es 0 (w = 0) o si no se evalúa ninguna herramienta (i = 0), el valor máximo de mitigación posible es 0[cite: 1, 2]. En esta implementación en Python, esto se maneja implícitamente inicializando la matriz dp completa con ceros antes de ejecutar la relación de recurrencia[cite: 1].

## Arquitectura y Ejecución
Para asegurar un diseño limpio y escalable, el código se dividió en dos módulos:
*   optimizer.py: Contiene exclusivamente el motor matemático, los estados y la reconstrucción de la solución óptima.
*   gui.py: Construye la interfaz gráfica mediante contenedores Frame y elementos Treeview de Tkinter, actuando como cliente de la lógica de negocio.

### Instrucciones de uso local
Al utilizar librerías estándar de Python, el proyecto no requiere instalación de dependencias externas.
1. Clonar el repositorio.
2. Abrir una terminal en la ruta del proyecto.
3. Ejecutar el aplicativo:
   ```bash
   python gui.py

### video: ### 3. https://www.youtube.com/watch?v=VNBN_h4TFcg&feature=youtu.be
