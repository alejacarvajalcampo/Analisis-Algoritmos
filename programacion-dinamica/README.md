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