# app.py
from flask import Flask, request, jsonify
from optimizer import optimizar_pipeline

app = Flask(__name__)

# Base de datos simulada de herramientas SQA disponibles
SUITES_DISPONIBLES = [
    ("Pruebas Unitarias (Pytest)", 2, 10),
    ("Análisis Estático (SonarQube)", 3, 15),
    ("Pruebas de Integración", 4, 20),
    ("Pruebas E2E (Playwright)", 5, 25),
    ("Auditoría Seguridad (OWASP ZAP)", 7, 40)
]

@app.route('/api/optimizar', methods=['POST'])
def optimizar():
    datos = request.get_json()
    
    # Validación de entrada
    if not datos or 'tiempo_limite' not in datos:
        return jsonify({"error": "Falta el parámetro 'tiempo_limite' en el JSON (minutos)"}), 400
        
    try:
        tiempo_limite = int(datos['tiempo_limite'])
    except ValueError:
        return jsonify({"error": "El tiempo límite debe ser un número entero"}), 400
    
    valor_total, seleccionadas, tiempo_usado = optimizar_pipeline(SUITES_DISPONIBLES, tiempo_limite)
    
    return jsonify({
        "mensaje": "Optimización calculada correctamente mediante Programación Dinámica",
        "parametros_entrada": {
            "tiempo_limite_solicitado": tiempo_limite
        },
        "resultados": {
            "valor_total_mitigacion": valor_total,
            "tiempo_total_usado": tiempo_usado,
            "suites_a_ejecutar": seleccionadas
        }
    })

if __name__ == '__main__':
    app.run(debug=True)