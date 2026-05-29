import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from funciones import limite_izquierda
from funciones import limite_derecha


from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

from rut import validar_rut_detallado
from rut import obtener_digitos
from rut import calcular_v

from conica import construir_ecuacion_detallado
from conica import clasificar_conica

from transformaciones import ecuacion_general
from transformaciones import forma_canonica

from funciones import analizar_limites
from funciones import construir_funcion

from evidencia import obtener_tabla

from graficas import graficar_desde_ecuacion


# =====================================================
# COLORES
# =====================================================

COLOR_FONDO = "#1e1e2f"
COLOR_PANEL = "#2b2b40"
COLOR_BOTON = "#4a90e2"
COLOR_TEXTO = "white"

FUENTE = ("Arial", 11)
FUENTE_TITULO = ("Arial", 18, "bold")


# =====================================================
# VENTANA PRINCIPAL
# =====================================================

ventana = tk.Tk()

ventana.title("Proyecto EID - Secciones Cónicas")
ventana.geometry("1400x850")

ventana.configure(bg=COLOR_FONDO)


# =====================================================
# PANEL IZQUIERDO
# =====================================================

panel_izq = tk.Frame(
    ventana,
    bg=COLOR_PANEL,
    width=500
)

panel_izq.pack(
    side="left",
    fill="y"
)

panel_izq.pack_propagate(False)


# =====================================================
# PANEL DERECHO
# =====================================================

panel_der = tk.Frame(
    ventana,
    bg="white"
)

panel_der.pack(
    side="right",
    fill="both",
    expand=True
)


# =====================================================
# TITULO
# =====================================================

titulo = tk.Label(
    panel_izq,
    text="Generador de\nSecciones Cónicas",
    bg=COLOR_PANEL,
    fg="white",
    font=FUENTE_TITULO
)

titulo.pack(pady=20)


# =====================================================
# INGRESO RUT
# =====================================================

label_rut = tk.Label(
    panel_izq,
    text="Ingrese RUT:",
    bg=COLOR_PANEL,
    fg="white",
    font=FUENTE
)

label_rut.pack()

entrada_rut = tk.Entry(
    panel_izq,
    width=30,
    font=("Arial", 12)
)

entrada_rut.pack(pady=10)


# =====================================================

# RESULTADOS

# =====================================================

frame_resultados = tk.Frame(
panel_izq,
bg=COLOR_PANEL
)

frame_resultados.pack(pady=10)

resultado_texto = tk.Text(
frame_resultados,
width=55,
height=15,
bg="#151521",
fg="white",
font=("Consolas", 10)
)

resultado_texto.pack(
side="left"
)

scroll_resultados = tk.Scrollbar(
frame_resultados,
command=resultado_texto.yview
)

scroll_resultados.pack(
side="right",
fill="y"
)

resultado_texto.config(
yscrollcommand=scroll_resultados.set
)




# =====================================================
# NOTEBOOK
# =====================================================

tabs = ttk.Notebook(panel_der)

tabs.pack(fill="both", expand=True)

tab_grafica = tk.Frame(tabs)
tab_limites = tk.Frame(tabs)

tabs.add(tab_grafica, text="Cónica")
tabs.add(tab_limites, text="Límites")


# =====================================================
# FRAME GRAFICA
# =====================================================

frame_grafica = tk.Frame(tab_grafica)

frame_grafica.pack(fill="both", expand=True)


# =====================================================
# TABLA LIMITES
# =====================================================

tabla = ttk.Treeview(
    tab_limites,
    columns=("x", "y"),
    show="headings",
    height=12
)

tabla.heading("x", text="x")
tabla.heading("y", text="f(x)")

tabla.column("x", width=150)
tabla.column("y", width=150)

tabla.pack(pady=20)


# =====================================================
# CAMPOS VACIOS DEFENSA
# =====================================================

frame_defensa = tk.Frame(
    tab_limites
)

frame_defensa.pack(pady=20)

campos = [
    "Límite izquierda",
    "Límite derecha",
    "¿Existe límite?",
    "Valor función",
    "¿Es continua?",
    "Tipo discontinuidad",
    "Justificación"
]

entries = {}

for campo in campos:

    fila = tk.Frame(frame_defensa)

    fila.pack(anchor="w", pady=5)

    label = tk.Label(
        fila,
        text=campo + ":",
        width=20,
        anchor="w"
    )

    label.pack(side="left")

    entrada = tk.Entry(
        fila,
        width=40
    )

    entrada.pack(side="left")

    entries[campo] = entrada


# =====================================================
# FUNCION PRINCIPAL
# =====================================================

def generar():

    rut = entrada_rut.get()

    if not validar_rut_detallado(rut):

        messagebox.showerror(
            "Error",
            "RUT inválido"
        )

        return

    # =================================================
    # LIMPIAR
    # =================================================

    resultado_texto.delete("1.0", tk.END)

    for item in tabla.get_children():

        tabla.delete(item)

    # =================================================
    # OBTENER DATOS
    # =================================================

    d, dv = obtener_digitos(rut)

    v = calcular_v(dv)

    A, B, C, D, E = construir_ecuacion_detallado(d, v)

    tipo = clasificar_conica(A, B)

    # =================================================
    # TEXTO
    # =================================================

    resultado_texto.insert(
        tk.END,
        "====================================\n"
    )

    resultado_texto.insert(
        tk.END,
        " ECUACION GENERAL\n"
    )

    resultado_texto.insert(
        tk.END,
        "====================================\n\n"
    )

    resultado_texto.insert(
        tk.END,
        ecuacion_general(A, B, C, D, E)
    )

    resultado_texto.insert(
        tk.END,
        f"\n\nTipo de cónica: {tipo}\n"
    )

    resultado_texto.insert(
        tk.END,
        "\n====================================\n"
    )

    resultado_texto.insert(
        tk.END,
        " ANALISIS DE LIMITES\n"
    )

    resultado_texto.insert(
        tk.END,
        "====================================\n\n"
    )

    # =================================================
    # FUNCIONES
    # =================================================

    datos_funcion = construir_funcion(d)

    resultado_texto.insert(
    tk.END,
    f"\nTipo de discontinuidad: {datos_funcion['tipo']}\n"
    )

    resultado_texto.insert(
    tk.END,
    f"Punto de análisis: x = {datos_funcion['a']}\n"
    )

    analizar_limites(d)
    izquierda = limite_izquierda(datos_funcion)
    derecha = limite_derecha(datos_funcion)

    resultado_texto.insert(
    tk.END,
    f"\nLímite por izquierda: {izquierda}\n"
    )

    resultado_texto.insert(
    tk.END,
    f"Límite por derecha: {derecha}\n"
    )
    if izquierda == derecha:

        resultado_texto.insert(
            tk.END,
            "\nEl límite existe.\n"
        )
    else:

        resultado_texto.insert(
            tk.END,
            "\nEl límite no existe.\n"
        )

    if datos_funcion["tipo"] == "removible":

        resultado_texto.insert(
            tk.END,
            "Discontinuidad removible.\n"
        )

    elif datos_funcion["tipo"] == "salto":

        resultado_texto.insert(
            tk.END,
            "Discontinuidad de salto.\n"
        )

    elif datos_funcion["tipo"] == "infinita":

        resultado_texto.insert(
            tk.END,
            "Discontinuidad infinita.\n"
        )

        resultado_texto.insert(
            tk.END,
            f"Asintota vertical: x = {datos_funcion['a']}\n"
        )

        




    tabla_datos = obtener_tabla(datos_funcion)

    for fila in tabla_datos:

        tabla.insert(
            "",
            "end",
            values=(
                fila["x"],
                fila["y"]
            )
        )

    # =================================================
    # GRAFICA
    # =================================================

    for widget in frame_grafica.winfo_children():

        widget.destroy()
    
    plt.close("all")

    fig = plt.figure(figsize=(7, 7))

    ax = fig.add_subplot(111)

    ax.set_title(f"{tipo}")

    ax.axhline(0)
    ax.axvline(0)

    ax.grid(True)

    ax.set_aspect("equal")

    # =================================================
    # GRAFICAR CONICA
    # =================================================

    try:

        graficar_desde_ecuacion(
            tipo.lower(),
            A,
            B,
            C,
            D,
            E
        )

    except:

        pass

    canvas = FigureCanvasTkAgg(
        fig,
        master=frame_grafica
    )

    canvas.draw()
    plt.close(fig)


    canvas.get_tk_widget().pack(
        fill="both",
        expand=True
    )


# =====================================================
# BOTON
# =====================================================

boton = tk.Button(
    panel_izq,
    text="Generar Proyecto",
    command=generar,
    bg=COLOR_BOTON,
    fg="white",
    font=("Arial", 12, "bold"),
    width=25,
    height=2
)

boton.pack(pady=20)


# =====================================================
# FOOTER
# =====================================================

footer = tk.Label(
    panel_izq,
    text="MAT1186 - Proyecto EID",
    bg=COLOR_PANEL,
    fg="gray"
)

footer.pack(side="bottom", pady=10)


# =====================================================

try:

    ventana.mainloop()

except KeyboardInterrupt:

    print("Programa finalizado.")

