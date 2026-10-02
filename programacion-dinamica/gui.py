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
    root = tk.Tk()
    root.title("Optimizador de Pipeline CI/CD - Programación Dinámica")
    root.geometry("550x400")
    root.configure(padx=20, pady=20)

    # Contenedor 1: Entrada de datos (Header)
    frame_top = tk.Frame(root)
    frame_top.pack(fill=tk.X, pady=(0, 15))

    tk.Label(frame_top, text="Presupuesto de Tiempo (min):", font=("Segoe UI", 10, "bold")).pack(side=tk.LEFT)
    entry_tiempo = tk.Entry(frame_top, width=10, font=("Segoe UI", 10))
    entry_tiempo.pack(side=tk.LEFT, padx=10)
    entry_tiempo.insert(0, "10") # Valor por defecto

    btn_optimizar = tk.Button(frame_top, text="Ejecutar Algoritmo", bg="#005A9E", fg="white", font=("Segoe UI", 9, "bold"), command=ejecutar_optimizacion)
    btn_optimizar.pack(side=tk.LEFT)

    # Contenedor 2: Resultados visuales (Tabla)
    frame_mid = tk.Frame(root)
    frame_mid.pack(fill=tk.BOTH, expand=True)

    columnas = ("Suite", "Tiempo", "Valor")
    tree = ttk.Treeview(frame_mid, columns=columnas, show="headings", height=8)

    tree.heading("Suite", text="Suite de Pruebas")
    tree.column("Suite", width=220, anchor=tk.W)
    tree.heading("Tiempo", text="Tiempo")
    tree.column("Tiempo", width=100, anchor=tk.CENTER)
    tree.heading("Valor", text="Valor SQA")
    tree.column("Valor", width=100, anchor=tk.CENTER)
    tree.pack(fill=tk.BOTH, expand=True)

    # Contenedor 3: Resumen final (Footer)
    frame_bottom = tk.Frame(root)
    frame_bottom.pack(fill=tk.X, pady=(15, 0))

    lbl_resultado = tk.Label(frame_bottom, text="Mitigación del riesgo lograda: 0 pts", font=("Segoe UI", 11, "bold"), fg="#107C10")
    lbl_resultado.pack(anchor=tk.W)

    lbl_tiempo = tk.Label(frame_bottom, text="Tiempo total utilizado: 0 minutos", font=("Segoe UI", 10))
    lbl_tiempo.pack(anchor=tk.W)

    if _name_ == "_main_":
        root.mainloop()