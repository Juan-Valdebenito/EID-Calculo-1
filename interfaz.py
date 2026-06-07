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

import rut
from transformaciones import ecuacion_general
from transformaciones import forma_canonica

from funciones import analizar_limites
from funciones import construir_funcion

from evidencia import obtener_tabla

from graficas import graficar_desde_ecuacion
from grafica_limites import graficar_funcion


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


frame_resultados.pack(pady=10, fill="both", expand=True, padx=20)
resultado_texto = tk.Text(
    frame_resultados,
    width=55,
    height=30,  
    bg="#151521",
    fg="white",
    font=("Consolas", 10)
)

resultado_texto.pack(
    side="left",
    fill="both",
    expand=True
)


# =====================================================
# NOTEBOOK
# =====================================================

tabs = ttk.Notebook(panel_der)

tabs.pack(fill="both", expand=True)

tab_grafica = tk.Frame(tabs)

canvas_conica = tk.Canvas(tab_grafica)
scroll_conica = tk.Scrollbar(
    tab_grafica,
    orient="vertical",
    command=canvas_conica.yview
)

frame_conica = tk.Frame(canvas_conica)

frame_conica.bind(
    "<Configure>",
    lambda e: canvas_conica.configure(
        scrollregion=canvas_conica.bbox("all")
    )
)

canvas_conica.create_window(
    (0, 0),
    window=frame_conica,
    anchor="nw"
)

canvas_conica.configure(
    yscrollcommand=scroll_conica.set
)


canvas_conica.pack(
    side="left",
    fill="both",
    expand=True
)

scroll_conica.pack(
    side="right",
    fill="y"
)

tab_limites = tk.Frame(tabs)

canvas_limites = tk.Canvas(tab_limites)

scroll_limites = tk.Scrollbar(
    tab_limites,
    orient="vertical",
    command=canvas_limites.yview
)

frame_limites = tk.Frame(canvas_limites)

frame_limites.bind(
    "<Configure>",
    lambda e: canvas_limites.configure(
        scrollregion=canvas_limites.bbox("all")
    )
)

canvas_limites.create_window(
    (0, 0),
    window=frame_limites,
    anchor="nw"
)

canvas_limites.configure(
    yscrollcommand=scroll_limites.set
)


canvas_limites.pack(
    side="left",
    fill="both",
    expand=True
)

scroll_limites.pack(
    side="right",
    fill="y"
)



tabs.add(tab_grafica, text="Cónica")
tabs.add(tab_limites, text="Límites")

def scroll_mouse(event):

    pestaña = tabs.index(tabs.select())

    if pestaña == 0:
        canvas_conica.yview_scroll(
            int(-1 * (event.delta / 120)),
            "units"
        )

    elif pestaña == 1:
        canvas_limites.yview_scroll(
            int(-1 * (event.delta / 120)),
            "units"
        )

ventana.bind_all(
    "<MouseWheel>",
    scroll_mouse
)

# =====================================================
# FRAME GRAFICA
# =====================================================

frame_grafica = tk.Frame(frame_conica)
frame_grafica.pack(fill="both", expand=True)

frame_elementos = tk.LabelFrame(
    frame_conica,
    text="Elementos Geométricos",
    padx=10,
    pady=10
)

frame_elementos.pack(
    fill="x",
    padx=10,
    pady=10
)

# ==========================================
# CAMPOS GEOMÉTRICOS
# ==========================================

elementos = {}

def actualizar_campos_conica(tipo):

    for widget in frame_elementos.winfo_children():
        widget.destroy()

    elementos.clear()

    if tipo.lower() == "circunferencia":

        campos = [
            "Centro",
            "Radio"
        ]

    elif tipo.lower() == "elipse":

        campos = [
            "Centro",
            "Vértices",
            "Focos",
            "Eje mayor",
            "Eje menor",
            "Excentricidad"
        ]

    elif tipo.lower() in ["hipérbola", "hiperbola"]:

        campos = [
            "Centro",
            "Vértices",
            "Focos",
            "Eje transverso",
            "Eje conjugado",
            "Asíntotas"
        ]

    elif tipo.lower() in ["parábola", "parabola"]:

        campos = [
            "Vértice",
            "Foco",
            "Directriz"
        ]

    else:

        campos = []

    for i, campo in enumerate(campos):

        tk.Label(
            frame_elementos,
            text=campo + ":"
        ).grid(
            row=i,
            column=0,
            sticky="w",
            padx=5,
            pady=3
        )

        entrada = tk.Entry(
            frame_elementos,
            width=50
        )

        entrada.grid(
            row=i,
            column=1,
            padx=5,
            pady=3
        )

        elementos[campo] = entrada

# --- GRÁFICA INICIAL VACÍA ---
fig_inicial, ax_inicial = plt.subplots(figsize=(7, 7))
ax_inicial.set_title("Esperando RUT...")
ax_inicial.axhline(0, color='black', linewidth=0.5)
ax_inicial.axvline(0, color='black', linewidth=0.5)
ax_inicial.grid(True)
ax_inicial.set_aspect("equal")

ax_inicial.set_xlim(-10, 10)
ax_inicial.set_ylim(-10, 10)

canvas_inicial = FigureCanvasTkAgg(fig_inicial, master=frame_grafica)
canvas_inicial.draw()
canvas_inicial.get_tk_widget().pack(fill="both", expand=True)

# ==========================================
# GRAFICA LIMITES
# ==========================================

frame_grafica_limites = tk.Frame(frame_limites)

frame_grafica_limites.pack(
    fill="both",
    expand=True
)

frame_explicacion_limites = tk.Frame(tab_limites, bg=COLOR_PANEL)
frame_explicacion_limites.pack(side="left", fill="both", expand=True, padx=10, pady=10)

label_limites_titulo = tk.Label(
    frame_explicacion_limites,
    text="Justificación Matemática del Límite",
    font=("Arial", 12, "bold"),
    bg=COLOR_PANEL,
    fg="white"
)
label_limites_titulo.pack(pady=5)

texto_limites_explicacion = tk.Text(
    frame_explicacion_limites,
    width=45,
    height=20,
    bg="#151521",
    fg="white",
    font=("Consolas", 10)
)
texto_limites_explicacion.pack(fill="both", expand=True, padx=5, pady=5)
texto_limites_explicacion.config(state="disabled")


# ------------------------------------

# =====================================================
# TABLA LIMITES
# =====================================================

tabla = ttk.Treeview(
    frame_limites,
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
    frame_limites
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

    # =================================
    # LIMPIAR SIEMPRE
    # =================================

    resultado_texto.delete("1.0", tk.END)

    for entrada in entries.values():
        entrada.delete(0, tk.END)

    for item in tabla.get_children():
        tabla.delete(item)

    # =================================
    # OBTENER RUT
    # =================================

    rut = entrada_rut.get()

    if rut.strip() == "":

        resultado_texto.insert(
            tk.END,
            "====================================\n"
        )

        resultado_texto.insert(
            tk.END,
            " ERROR\n"
        )

        resultado_texto.insert(
            tk.END,
            "====================================\n\n"
        )

        resultado_texto.insert(
            tk.END,
            "Debe ingresar un RUT.\n"
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

    if d is None:

        resultado_texto.delete("1.0", tk.END)

        resultado_texto.insert(
            tk.END,
            "====================================\n"
            )

        resultado_texto.insert(
            tk.END,
            " ERROR\n"
            )

        resultado_texto.insert(
            tk.END,
            "====================================\n\n"
            )

        resultado_texto.insert(
            tk.END,
            "Formato de RUT inválido.\n"
        )

        return

    v = calcular_v(dv)

    A, B, C, D, E = construir_ecuacion_detallado(d, v)

    tipo = clasificar_conica(A, B)
    
    actualizar_campos_conica(tipo)

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

    resultado_texto.insert(
    tk.END,
    "\n====================================\n"
    )

    resultado_texto.insert(
        tk.END,
        " FUNCIÓN GENERADA\n"
    )

    resultado_texto.insert(
        tk.END,
        "====================================\n\n"
    )

    resultado_texto.insert(
        tk.END,
        f"{datos_funcion['funcion']}\n"
    )

    resultado_texto.insert(
        tk.END,
        "\n====================================\n"
    )

    resultado_texto.insert(
        tk.END,
        " REGLA APLICADA\n"
    )

    resultado_texto.insert(
        tk.END,
        "====================================\n\n"
    )

    resultado_texto.insert(
        tk.END,
        f"{datos_funcion['regla']}\n"
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

    fig = graficar_desde_ecuacion(tipo.lower(), A, B, C, D, E)

    if fig is None:
        label_error = tk.Label(
            frame_grafica, 
            text="Caso degenerado detectado.\nNo se puede generar gráfica real.", 
            font=("Arial", 14),
            bg="white"
        )
        label_error.pack(expand=True)
        return
    
    canvas = FigureCanvasTkAgg(fig, master=frame_grafica)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)

    # ==========================================
    # GRAFICA DE LIMITES
    # ==========================================

    for widget in frame_grafica_limites.winfo_children():
        widget.destroy()
        
    plt.close("all")

    fig_limites = graficar_funcion(datos_funcion)

    canvas_limites = FigureCanvasTkAgg(
        fig_limites,
        master=frame_grafica_limites
    )

    canvas_limites.draw()

    canvas_limites.get_tk_widget().pack(
        fill="both",
        expand=True
    )

    # ==================================================
    # INTEGRACIÓN DE JUSTIFICACIÓN DE LÍMITES EN LA UI
    # ==================================================
    
    texto_limites_explicacion.config(state="normal")
    texto_limites_explicacion.delete("1.0", tk.END)
    
    resto_calculado = d[7] % 3 
    tipo_discontinuidad = datos_funcion["tipo"]
    punto_a = datos_funcion["a"]
    izq_val = limite_izquierda(datos_funcion)
    der_val = limite_derecha(datos_funcion)
    
    reporte = "========================================================\n"
    reporte += "              REPORTE ANALÍTICO DE LÍMITES              \n"
    reporte += "========================================================\n\n"
    reporte += f"• Punto Crítico de Análisis (a): x = {punto_a}\n"
    reporte += f"• Criterio del RUT (d8 % 3): {resto_calculado}\n"
    reporte += f"• Tipo de Discontinuidad: {tipo_discontinuidad.upper()}\n\n"
    reporte += f"-> Límite por la izquierda (x -> {punto_a}-): {izq_val}\n"
    reporte += f"-> Límite por la derecha   (x -> {punto_a}+): {der_val}\n\n"
    reporte += "--------------------------------------------------------\n"
    reporte += "CONCLUSIÓN Y JUSTIFICACIÓN MATEMÁTICA:\n"
    reporte += "--------------------------------------------------------\n\n"
    
    if tipo_discontinuidad == "removible":
        reporte += f"Como los límites laterales existen y son iguales ({izq_val} = {der_val}),\n"
        reporte += f"el límite general EXISTE y vale {izq_val}.\n\n"
        reporte += f"Sin embargo, la función NO está definida en el punto x = {punto_a}.\n"
        reporte += f"Por lo tanto, se presenta una DISCONTINUIDAD REMOVIBLE."
        
    elif tipo_discontinuidad == "salto":
        reporte += f"Al aproximarse al punto crítico x = {punto_a}, los límites\n"
        reporte += f"laterales tienden a valores finitos pero distintos ({izq_val} ≠ {der_val}).\n\n"
        reporte += f"Dado que los caminos no coinciden, el límite general NO EXISTE.\n"
        reporte += f"Esto genera una DISCONTINUIDAD DE SALTO FINITO."
        
    elif tipo_discontinuidad == "infinita":
        reporte += f"Se observa que al menos uno de los límites laterales crece\n"
        reporte += f"o decrece sin cota hacia el infinito.\n\n"
        reporte += f"La recta x = {punto_a} actúa como ASÍNTOTA VERTICAL, generando\n"
        reporte += f"una DISCONTINUIDAD INFINITA."

    texto_limites_explicacion.insert("1.0", reporte)
    texto_limites_explicacion.config(state="disabled")
    
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

