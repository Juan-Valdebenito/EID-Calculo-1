import tkinter as tk
from tkinter import messagebox

from rut import validar_rut_detallado, obtener_digitos, calcular_v
from conica import construir_ecuacion_detallado, clasificar_conica
from transformaciones import ecuacion_general
from graficas import graficar_desde_ecuacion


def generar():

    rut = entrada_rut.get()

    if not validar_rut_detallado(rut):

        messagebox.showerror("Error", "RUT inválido")
        return

    d, dv = obtener_digitos(rut)

    v = calcular_v(dv)

    A, B, C, D, E = construir_ecuacion_detallado(d, v)

    tipo = clasificar_conica(A, B).lower()

    resultado.set(
        "Ecuación:\n"
        + ecuacion_general(A, B, C, D, E)
        + "\n\nTipo: "
        + tipo
    )

    graficar_desde_ecuacion(tipo, A, B, C, D, E)


# =========================
# VENTANA
# =========================

ventana = tk.Tk()

ventana.title("EID - Secciones Cónicas")
ventana.geometry("500x300")

# =========================
# TITULO
# =========================

titulo = tk.Label(
    ventana,
    text="Generador de Secciones Cónicas",
    font=("Arial", 16)
)

titulo.pack(pady=10)

# =========================
# ENTRADA RUT
# =========================

entrada_rut = tk.Entry(ventana, width=30)

entrada_rut.pack(pady=10)

# =========================
# BOTON
# =========================

boton = tk.Button(
    ventana,
    text="Generar gráfica",
    command=generar
)

boton.pack(pady=10)

# =========================
# RESULTADOS
# =========================

resultado = tk.StringVar()

label_resultado = tk.Label(
    ventana,
    textvariable=resultado,
    justify="left"
)

label_resultado.pack(pady=20)

# =========================

ventana.mainloop()