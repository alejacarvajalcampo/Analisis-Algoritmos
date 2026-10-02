# gui.py
import tkinter as tk
from tkinter import messagebox, ttk
from optimizer import optimizar_pipeline

# Base de datos simulada de herramientas SQA disponibles
SUITES_DISPONIBLES = [
    ("Pruebas Unitarias (Pytest)", 2, 10),
    ("Análisis Estático (SonarQube)", 3, 15),
    ("Pruebas de Integración", 4, 20),
    ("Pruebas E2E (Playwright)", 5, 25),
    ("Auditoría Seguridad (OWASP ZAP)", 7, 40)
]

def ejecutar_optimizacion():
    try:
        tiempo_limite = int(entry_tiempo.get())
        if tiempo_limite <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error de validación", "Por favor, ingresa un número entero mayor a 0.")
        return

    valor_total, seleccionadas, tiempo_usado = optimizar_pipeline(SUITES_DISPONIBLES, tiempo_limite)

    for row in tree.get_children():
        tree.delete(row)

    for item in seleccionadas:
        tree.insert("", tk.END, values=(item['suite'], f"{item['tiempo_minutos']} min", f"{item['valor_mitigacion']} pts"))

    lbl_resultado.config(text=f"Mitigación del riesgo lograda: {valor_total} pts")
    lbl_tiempo.config(text=f"Tiempo total utilizado: {tiempo_usado} minutos")