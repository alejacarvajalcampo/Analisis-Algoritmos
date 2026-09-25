# Detección de Anomalías Transaccionales mediante Teoría de Grafos

## 1. Planteamiento del Problema

El presente proyecto plantea una solución computacional enfocada en la ciberseguridad financiera: la detección de lavado de activos y la técnica de distribución de fondos conocida como **"smurfing"** (o pitufeo).

Este patrón consiste en la emisión de múltiples transferencias en lapsos de tiempo muy cortos hacia diversas cuentas de destino catalogadas como sospechosas o de dudosa procedencia, buscando evadir los controles de montos máximos. La detección en tiempo real de estas ramificaciones suele generar cuellos de botella al utilizar consultas relacionales estándar, lo que justifica la aplicación de **estructuras de datos no lineales** para optimizar el rendimiento de la búsqueda.

---

## 2. Algoritmo de Grafos Seleccionado y Funcionamiento

Se diseñó un algoritmo basado en la **Teoría de Grafos** que monitorea el comportamiento transaccional en tiempo real. El algoritmo evalúa el **grado de salida (*out-degree*)** de un vértice específico, restringido a un subgrafo delimitado por una ventana temporal.

### Funcionamiento del Algoritmo

1. **Modelado matemático:** La red bancaria se representa como un **grafo dirigido** $G = (V, E)$:
    * **Vértices ($V$):** Cuentas bancarias.
    * **Aristas dirigidas ($E$):** Transferencias realizadas, almacenando el monto y la marca temporal (*timestamp*).
2. **Estructura de datos:** Para manejar la dispersión de la red bancaria, se implementó una **lista de adyacencia**. Esto permite consultar y registrar las conexiones salientes de cualquier vértice con una complejidad temporal eficiente de $O(1)$ para la inserción.
3. **Filtrado de subgrafo temporal:** Cada vez que se añade una nueva arista, el algoritmo delimita el grafo aislando únicamente las conexiones emitidas por el vértice de origen en una ventana temporal de los últimos **60 segundos**.
4. **Detección de anomalías:** Sobre este subgrafo reciente, se calcula el grado de salida dirigido exclusivamente hacia vértices catalogados previamente como **"sospechosos"**. Si este valor alcanza o supera el umbral establecido ($\ge 3$ conexiones a nodos distintos), se detecta un patrón anómalo y se dispara una alerta.

---

## 3. Arquitectura e Implementación

El proyecto se desarrolló bajo una arquitectura cliente-servidor:

* **Backend (Lógica del Grafo):** Desarrollado en **Python** haciendo uso del framework **FastAPI**. Esta capa mantiene en memoria la lista de adyacencia, ejecuta los cálculos de grado de salida restringidos por tiempo y expone los resultados a través de una API REST.
* **Frontend (Vista del Usuario):** Desarrollado con **React**. Proporciona una interfaz interactiva donde se simulan las transferencias en tiempo real y se evidencia el bloqueo/alerta de las operaciones al cumplirse la condición matemática.

---

## 4. Instrucciones de Ejecución

Para desplegar el proyecto en un entorno local, sigue los siguientes pasos en dos terminales independientes:

### Backend (Servidor)

1. Navega al directorio del backend:
```bash
cd backend
```

2. Activa el entorno virtual de Python:
- Windows:
```bash
venv\Scripts\activate
```
- Linux/macOS:
```bash
source venv/bin/activate
```

3. Instala las dependencias requeridas (si cuentas con requirements.txt):
```bash
pip install -r requirements.txt
```
*(Nota: Si no usaste un archivo requirements.txt, instala las dependencias directamente con: `pip install fastapi uvicorn pydantic`)*

4. Inicia el servidor de desarrollo:
```bash
uvicorn main:app --reload
```

### Frontend (Cliente)

1. Navega al directorio del frontend:
```bash
cd frontend
```

2. Instala los paquetes de Node:
```bash
npm install
```

3. Inicia el entorno de desarrollo:
```bash
npm run dev
```

---

## 5. Sustentación

🎥 **Enlace al video de sustentación:** https://youtu.be/uDxAjsE3SkY

En el video adjunto se explica el problema planteado, la justificación de la estructura de datos elegida, su funcionamiento interno en memoria y la demostración práctica con la interfaz web.