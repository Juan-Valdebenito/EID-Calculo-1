import tkinter as tk
from tkinter import ttk

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from conica import clasificar_conica, construir_ecuacion_detallado
from evidencia import obtener_tabla
from funciones import analizar_limites, construir_funcion
from grafica_limites import graficar_funcion
from graficas import graficar_desde_ecuacion
from rut import calcular_v, obtener_digitos, validar_rut_detallado
from transformaciones import ecuacion_general, forma_canonica, procedimiento_canonica_a_general


# =====================================================
# COLORES Y ESTILO
# =====================================================

COLOR_FONDO = "#eef8f6"
COLOR_PANEL = "#063b3f"
COLOR_PANEL_2 = "#0b5559"
COLOR_TEXTO = "#f3fffb"
COLOR_MUTED = "#a9d9d1"
COLOR_BOTON = "#0f9f8f"
COLOR_BOTON_HOVER = "#0a7f75"
COLOR_CORRECTO = "#087f5b"
COLOR_ERROR = "#b42318"
COLOR_SUPERFICIE = "#fbfffd"
COLOR_SUPERFICIE_2 = "#e0f2ef"
COLOR_LINEA = "#b9ddd8"
FUENTE = ("Arial", 10)
FUENTE_TITULO = ("Arial", 18, "bold")
FUENTE_SECCION = ("Arial", 11, "bold")
FUENTE_MONO = ("Consolas", 10)


sesion_evaluacion = {"valores_reales": {}, "widgets_entry": {}}


# =====================================================
# HELPERS DE INTERFAZ
# =====================================================

def aplicar_estilos():
    style = ttk.Style()
    style.theme_use("clam")

    style.configure(
        "TNotebook",
        background=COLOR_FONDO,
        borderwidth=0,
    )
    style.configure(
        "TNotebook.Tab",
        padding=(14, 8),
        font=("Arial", 10, "bold"),
        background=COLOR_SUPERFICIE_2,
        foreground="#0f3f43",
    )
    style.map(
        "TNotebook.Tab",
        background=[("selected", COLOR_SUPERFICIE)],
        foreground=[("selected", COLOR_BOTON)],
    )
    style.configure(
        "Treeview",
        rowheight=24,
        font=FUENTE,
        background=COLOR_SUPERFICIE,
        fieldbackground=COLOR_SUPERFICIE,
    )
    style.configure(
        "Treeview.Heading",
        font=("Arial", 10, "bold"),
        background=COLOR_SUPERFICIE_2,
        foreground="#0f3f43",
    )


def crear_texto(parent, height=12):
    texto = tk.Text(
        parent,
        height=height,
        wrap="word",
        bg=COLOR_SUPERFICIE,
        fg="#0b2528",
        insertbackground="#0b2528",
        relief="solid",
        bd=1,
        font=FUENTE_MONO,
        padx=10,
        pady=10,
    )
    texto.pack(fill="both", expand=True, padx=10, pady=10)
    texto.config(state="disabled")
    return texto


def escribir(texto_widget, contenido):
    texto_widget.config(state="normal")
    texto_widget.delete("1.0", tk.END)
    texto_widget.insert("1.0", contenido)
    texto_widget.config(state="disabled")


def limpiar_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()


def mostrar_figura(frame, fig):
    limpiar_frame(frame)
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)
    return canvas


def crear_estado(parent, titulo, valor="-"):
    contenedor = tk.Frame(parent, bg=COLOR_PANEL_2)
    contenedor.pack(fill="x", padx=16, pady=5)

    tk.Label(
        contenedor,
        text=titulo,
        bg=COLOR_PANEL_2,
        fg=COLOR_MUTED,
        font=("Arial", 9, "bold"),
        anchor="w",
    ).pack(fill="x")

    label = tk.Label(
        contenedor,
        text=valor,
        bg=COLOR_PANEL_2,
        fg=COLOR_TEXTO,
        font=FUENTE,
        anchor="w",
        justify="left",
        wraplength=250,
    )
    label.pack(fill="x", pady=(2, 0))
    return label


def boton_menu(parent, texto, comando):
    boton = tk.Button(
        parent,
        text=texto,
        command=comando,
        bg=COLOR_PANEL_2,
        activebackground=COLOR_PANEL_2,
        fg=COLOR_TEXTO,
        activeforeground=COLOR_TEXTO,
        relief="flat",
        font=("Arial", 10, "bold"),
        anchor="w",
        padx=18,
        pady=10,
        bd=0,
        highlightthickness=1,
        highlightbackground="#12746d",
        highlightcolor="#33cabb",
        cursor="hand2",
    )
    boton.pack(fill="x", padx=10, pady=2)
    return boton


def seccion(parent, texto):
    tk.Label(
        parent,
        text=texto.upper(),
        bg=COLOR_PANEL,
        fg=COLOR_MUTED,
        font=("Arial", 8, "bold"),
        anchor="w",
    ).pack(fill="x", padx=18, pady=(16, 4))


def titulo_panel(parent, texto):
    tk.Label(
        parent,
        text=texto,
        bg=COLOR_SUPERFICIE,
        fg="#0b2528",
        font=FUENTE_SECCION,
        anchor="w",
    ).pack(fill="x", padx=10, pady=(10, 0))


def figura_inicial(titulo):
    fig, ax = plt.subplots(figsize=(7, 4.6))
    ax.set_title(titulo)
    ax.axhline(0, color="#0b2528", linewidth=0.7)
    ax.axvline(0, color="#0b2528", linewidth=0.7)
    ax.grid(True, color="#c7e5e0")
    ax.set_aspect("equal")
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    return fig


# =====================================================
# EVALUACION INTERACTIVA DE CONICAS
# =====================================================

def verificar_fila_evaluacion(claves):
    valores_reales = sesion_evaluacion["valores_reales"]
    widgets_entry = sesion_evaluacion["widgets_entry"]

    for clave in claves:
        if clave not in widgets_entry:
            continue

        entry = widgets_entry[clave]
        valor_usuario = entry.get().strip()
        valor_correcto = valores_reales.get(clave, 0)
        es_correcto = False

        try:
            es_correcto = abs(float(valor_usuario) - float(valor_correcto)) < 0.05
        except ValueError:
            es_correcto = valor_usuario.lower() == str(valor_correcto).lower()

        entry.config(
            fg=COLOR_CORRECTO if es_correcto else COLOR_ERROR,
            font=("Arial", 10, "bold"),
        )
        entry.delete(0, tk.END)
        entry.insert(0, "Correcto" if es_correcto else f"Error: {valor_correcto}")


def mostrar_campos_evaluacion(frame_campos_dinamicos, tipo, A, B, C, D, E):
    limpiar_frame(frame_campos_dinamicos)
    sesion_evaluacion["valores_reales"] = {}
    sesion_evaluacion["widgets_entry"] = {}

    tipo_normalizado = tipo.lower()
    valores_reales = {}
    estructura_filas = []

    def sqrt_segura(val):
        return val ** 0.5 if val > 0 else 0

    if tipo_normalizado.startswith(("circunferencia", "elipse", "hip")) and A != 0 and B != 0:
        h_val = -C / (2 * A)
        k_val = -D / (2 * B)
        constante = -E + (C ** 2) / (4 * A) + (D ** 2) / (4 * B)

        valores_reales["Centro H"] = round(h_val, 2)
        valores_reales["Centro K"] = round(k_val, 2)
        estructura_filas.append({"tipo": "pair", "lbl1": "Centro H", "lbl2": "Centro K", "keys": ["Centro H", "Centro K"]})

        if tipo_normalizado.startswith("circunferencia"):
            valores_reales["Radio"] = round(sqrt_segura(constante / A), 2)
            estructura_filas.append({"tipo": "single", "lbl": "Radio", "key": "Radio"})

        elif tipo_normalizado.startswith("elipse"):
            a2, b2 = constante / A, constante / B
            if abs(a2) >= abs(b2):
                a_param = sqrt_segura(abs(a2))
                b_param = sqrt_segura(abs(b2))
                c_param = sqrt_segura(abs(a2) - abs(b2))
                f1_x, f1_y = h_val - c_param, k_val
                f2_x, f2_y = h_val + c_param, k_val
            else:
                a_param = sqrt_segura(abs(b2))
                b_param = sqrt_segura(abs(a2))
                c_param = sqrt_segura(abs(b2) - abs(a2))
                f1_x, f1_y = h_val, k_val - c_param
                f2_x, f2_y = h_val, k_val + c_param

            valores_reales["Foco 1 X"] = round(f1_x, 2)
            valores_reales["Foco 1 Y"] = round(f1_y, 2)
            valores_reales["Foco 2 X"] = round(f2_x, 2)
            valores_reales["Foco 2 Y"] = round(f2_y, 2)
            valores_reales["Eje Mayor"] = round(2 * a_param, 2)
            valores_reales["Eje Menor"] = round(2 * b_param, 2)
            valores_reales["Excentricidad"] = round(c_param / a_param, 2) if a_param > 0 else 0

            estructura_filas.extend([
                {"tipo": "pair", "lbl1": "Foco 1 X", "lbl2": "Foco 1 Y", "keys": ["Foco 1 X", "Foco 1 Y"]},
                {"tipo": "pair", "lbl1": "Foco 2 X", "lbl2": "Foco 2 Y", "keys": ["Foco 2 X", "Foco 2 Y"]},
                {"tipo": "single", "lbl": "Eje Mayor", "key": "Eje Mayor"},
                {"tipo": "single", "lbl": "Eje Menor", "key": "Eje Menor"},
                {"tipo": "single", "lbl": "Excentricidad", "key": "Excentricidad"},
            ])

        elif tipo_normalizado.startswith("hip"):
            a_param = sqrt_segura(abs(constante / A))
            b_param = sqrt_segura(abs(constante / B))
            m_val = (b_param / a_param) if A > 0 else (a_param / b_param)

            valores_reales["Eje Transverso"] = round(2 * a_param, 2)
            valores_reales["Eje Conjugado"] = round(2 * b_param, 2)
            valores_reales["Asíntota 1 (m)"] = round(m_val, 2)
            valores_reales["Asíntota 2 (m)"] = round(-m_val, 2)

            estructura_filas.extend([
                {"tipo": "single", "lbl": "Eje Transverso", "key": "Eje Transverso"},
                {"tipo": "single", "lbl": "Eje Conjugado", "key": "Eje Conjugado"},
                {"tipo": "pair", "lbl1": "Asíntota 1 (m)", "lbl2": "Asíntota 2 (m)", "keys": ["Asíntota 1 (m)", "Asíntota 2 (m)"]},
            ])

    elif tipo_normalizado.startswith("par"):
        if A == 0 and B != 0:
            k_val = -D / (2 * B)
            h_val = (-E + (D ** 2) / (4 * B)) / C if C != 0 else 0
            p_val = -C / (4 * B)
            f_x, f_y = h_val + p_val, k_val
            dir_val = h_val - p_val
        else:
            h_val = -C / (2 * A)
            k_val = (-E + (C ** 2) / (4 * A)) / D if D != 0 else 0
            p_val = -D / (4 * A)
            f_x, f_y = h_val, k_val + p_val
            dir_val = k_val - p_val

        valores_reales["Vértice H"] = round(h_val, 2)
        valores_reales["Vértice K"] = round(k_val, 2)
        valores_reales["Foco X"] = round(f_x, 2)
        valores_reales["Foco Y"] = round(f_y, 2)
        valores_reales["Directriz"] = round(dir_val, 2)

        estructura_filas.extend([
            {"tipo": "pair", "lbl1": "Vértice H", "lbl2": "Vértice K", "keys": ["Vértice H", "Vértice K"]},
            {"tipo": "pair", "lbl1": "Foco X", "lbl2": "Foco Y", "keys": ["Foco X", "Foco Y"]},
            {"tipo": "single", "lbl": "Directriz", "key": "Directriz"},
        ])

    sesion_evaluacion["valores_reales"] = valores_reales

    if not estructura_filas:
        tk.Label(
            frame_campos_dinamicos,
            text="No hay elementos geometricos evaluables para este caso.",
            bg=COLOR_SUPERFICIE,
            fg="#47615e",
            font=FUENTE,
        ).pack(anchor="w", padx=10, pady=10)
        return

    for fila in estructura_filas:
        row_frame = tk.Frame(frame_campos_dinamicos, bg=COLOR_SUPERFICIE)
        row_frame.pack(fill="x", pady=4, padx=10)

        claves = fila.get("keys", [fila.get("key")])
        items = (
            [(fila["lbl1"], claves[0]), (fila["lbl2"], claves[1])]
            if fila["tipo"] == "pair"
            else [(fila["lbl"], fila["key"])]
        )

        for label_text, key in items:
            tk.Label(
                row_frame,
                text=f"{label_text}:",
                font=FUENTE,
                bg=COLOR_SUPERFICIE,
                fg="#0b2528",
                width=15,
                anchor="e",
            ).pack(side="left", padx=(0, 5))

            entry = tk.Entry(
                row_frame,
                font=FUENTE,
                width=12,
                relief="solid",
                bd=1,
                bg="#f7fffc",
                fg="#0b2528",
                insertbackground="#0b2528",
                highlightthickness=1,
                highlightbackground=COLOR_LINEA,
                highlightcolor=COLOR_BOTON,
            )
            entry.pack(side="left", padx=(0, 10))
            entry.bind("<Button-1>", lambda _e, ent=entry: (ent.config(fg="#0b2528", font=FUENTE), ent.delete(0, tk.END)))
            sesion_evaluacion["widgets_entry"][key] = entry

        tk.Button(
            row_frame,
            text="Verificar",
            command=lambda k=claves: verificar_fila_evaluacion(k),
            bg=COLOR_BOTON,
            activebackground=COLOR_BOTON_HOVER,
            fg="#ffffff",
            activeforeground="#ffffff",
            font=("Arial", 9, "bold"),
            relief="flat",
            padx=12,
            pady=5,
            bd=0,
            highlightthickness=1,
            highlightbackground="#7fd2c8",
            cursor="hand2",
        ).pack(side="left", padx=4)


# =====================================================
# TEXTOS DE REPORTE
# =====================================================

def construir_reporte_rut(rut_ingresado, valido, detalle):
    estado = "Valido" if valido else "Invalido"
    return (
        "RUT\n"
        "====================================\n"
        "Ingreso\n"
        f"{rut_ingresado}\n\n"
        "Validacion\n"
        f"Estado: {estado}\n\n"
        "Procedimiento modulo 11\n"
        f"{detalle.strip()}\n"
    )


def construir_reporte_conicas(A, B, C, D, E, procedimiento_conica, tipo):
    return (
        "CONICAS\n"
        "====================================\n"
        "Ecuacion general\n"
        f"{ecuacion_general(A, B, C, D, E)}\n\n"
        "Procedimiento\n"
        f"{procedimiento_conica}\n\n"
        "Forma canonica\n"
        f"{forma_canonica(A, B, C, D, E)}\n\n"
        "Clasificacion\n"
        f"{tipo}\n\n"
        "Grafica\n"
        "Disponible en la pestaña Grafica > Conica.\n"
    )


def construir_reporte_transformaciones(A, B, C, D, E):
    return (
        "TRANSFORMACIONES\n"
        "====================================\n"
        "Procedimiento\n"
        "Se transforma desde la ecuacion general completando cuadrados hasta llegar a la forma canonica.\n\n"
        f"{forma_canonica(A, B, C, D, E)}\n\n"
        "Grafica original\n"
        "Disponible en la pestaña Grafica > Original.\n\n"
        "Grafica transformada\n"
        "Disponible en la pestaña Grafica > Transformada.\n"
    )


def construir_reporte_limites(datos_funcion, resultado_limites, tabla_datos):
    punto_a = datos_funcion["a"]
    tipo_discontinuidad = datos_funcion["tipo"]
    izq_val = resultado_limites["izquierda"]
    der_val = resultado_limites["derecha"]

    evidencia = ["x".ljust(14) + "f(x)"]
    evidencia.append("-" * 30)
    for fila in tabla_datos:
        evidencia.append(str(fila["x"]).ljust(14) + str(fila["y"]))

    if tipo_discontinuidad == "removible":
        conclusion = (
            f"Los limites laterales coinciden ({izq_val} = {der_val}), "
            "pero la funcion no esta definida en el punto. Hay discontinuidad removible."
        )
    elif tipo_discontinuidad == "salto":
        conclusion = (
            f"Los limites laterales son finitos y distintos ({izq_val} != {der_val}). "
            "El limite general no existe. Hay discontinuidad de salto."
        )
    else:
        conclusion = (
            f"La funcion diverge cerca de x = {punto_a}. "
            "Hay una asintota vertical y discontinuidad infinita."
        )

    return (
        "LIMITES\n"
        "====================================\n"
        "Construccion\n"
        f"{datos_funcion['procedimiento']}\n\n"
        "Limites laterales\n"
        f"Limite por izquierda: {izq_val}\n"
        f"Limite por derecha:   {der_val}\n"
        f"Existe limite:        {'Si' if resultado_limites['existe_limite'] else 'No'}\n"
        f"Valor funcion:        {resultado_limites['valor_funcion']}\n"
        f"Continua:             {'Si' if resultado_limites['continua'] else 'No'}\n\n"
        "Evidencia computacional\n"
        f"{chr(10).join(evidencia)}\n\n"
        "Grafica\n"
        "Disponible en la pestaña Grafica > Limites.\n\n"
        "Conclusion\n"
        f"{conclusion}\n"
    )


# =====================================================
# APLICACION
# =====================================================

def iniciar_app():
    ventana = tk.Tk()
    aplicar_estilos()

    ventana.title("Proyecto EID - Calculo 1")
    ventana.geometry("1240x820")
    ventana.minsize(1050, 720)
    ventana.configure(bg=COLOR_FONDO)
    ventana.grid_columnconfigure(1, weight=1)
    ventana.grid_rowconfigure(0, weight=1)

    panel_izq = tk.Frame(ventana, bg=COLOR_PANEL, width=310)
    panel_izq.grid(row=0, column=0, sticky="ns")
    panel_izq.grid_propagate(False)

    panel_der = tk.Frame(ventana, bg=COLOR_FONDO)
    panel_der.grid(row=0, column=1, sticky="nsew")
    panel_der.grid_columnconfigure(0, weight=1)
    panel_der.grid_rowconfigure(0, weight=3)
    panel_der.grid_rowconfigure(1, weight=2)

    tk.Label(
        panel_izq,
        text="Proyecto EID",
        bg=COLOR_PANEL,
        fg=COLOR_TEXTO,
        font=FUENTE_TITULO,
        anchor="w",
    ).pack(fill="x", padx=18, pady=(18, 4))

    tk.Label(
        panel_izq,
        text="Menu lateral",
        bg=COLOR_PANEL,
        fg=COLOR_MUTED,
        font=FUENTE,
        anchor="w",
    ).pack(fill="x", padx=18)

    seccion(panel_izq, "RUT")
    tk.Label(
        panel_izq,
        text="Ingreso",
        bg=COLOR_PANEL,
        fg=COLOR_TEXTO,
        font=FUENTE,
        anchor="w",
    ).pack(fill="x", padx=18, pady=(0, 4))

    entrada_rut = tk.Entry(
        panel_izq,
        width=24,
        font=("Arial", 12),
        relief="flat",
        bg="#f7fffc",
        fg="#0b2528",
        insertbackground="#0b2528",
        bd=0,
        highlightthickness=2,
        highlightbackground="#12746d",
        highlightcolor="#33cabb",
    )
    entrada_rut.pack(fill="x", padx=18, ipady=7)

    seccion(panel_izq, "Secciones")

    estado_rut = crear_estado(panel_izq, "Validacion", "Sin RUT ingresado")
    estado_conica = crear_estado(panel_izq, "Conicas", "Esperando generacion")
    estado_limite = crear_estado(panel_izq, "Limites", "Esperando generacion")

    frame_grafica = tk.LabelFrame(
        panel_der,
        text="Grafica",
        bg=COLOR_SUPERFICIE,
        fg="#0b2528",
        font=FUENTE_SECCION,
        padx=10,
        pady=10,
        bd=1,
        relief="solid",
    )
    frame_grafica.grid(row=0, column=0, sticky="nsew", padx=14, pady=(14, 7))
    frame_grafica.grid_columnconfigure(0, weight=1)
    frame_grafica.grid_rowconfigure(0, weight=1)

    tabs_grafica = ttk.Notebook(frame_grafica)
    tabs_grafica.grid(row=0, column=0, sticky="nsew")

    tab_grafica_conica = tk.Frame(tabs_grafica, bg=COLOR_SUPERFICIE)
    tab_grafica_original = tk.Frame(tabs_grafica, bg=COLOR_SUPERFICIE)
    tab_grafica_transformada = tk.Frame(tabs_grafica, bg=COLOR_SUPERFICIE)
    tab_grafica_limites = tk.Frame(tabs_grafica, bg=COLOR_SUPERFICIE)

    tabs_grafica.add(tab_grafica_conica, text="Conica")
    tabs_grafica.add(tab_grafica_original, text="Original")
    tabs_grafica.add(tab_grafica_transformada, text="Transformada")
    tabs_grafica.add(tab_grafica_limites, text="Limites")

    frame_evaluacion = tk.LabelFrame(
        panel_der,
        text="Evaluacion",
        bg=COLOR_SUPERFICIE,
        fg="#0b2528",
        font=FUENTE_SECCION,
        padx=10,
        pady=10,
        bd=1,
        relief="solid",
    )
    frame_evaluacion.grid(row=1, column=0, sticky="nsew", padx=14, pady=(7, 14))
    frame_evaluacion.grid_columnconfigure(0, weight=1)
    frame_evaluacion.grid_rowconfigure(0, weight=1)

    tabs_evaluacion = ttk.Notebook(frame_evaluacion)
    tabs_evaluacion.grid(row=0, column=0, sticky="nsew")

    tab_rut = tk.Frame(tabs_evaluacion, bg=COLOR_SUPERFICIE)
    tab_conicas = tk.Frame(tabs_evaluacion, bg=COLOR_SUPERFICIE)
    tab_transformaciones = tk.Frame(tabs_evaluacion, bg=COLOR_SUPERFICIE)
    tab_limites = tk.Frame(tabs_evaluacion, bg=COLOR_SUPERFICIE)

    tabs_evaluacion.add(tab_rut, text="RUT")
    tabs_evaluacion.add(tab_conicas, text="Conicas")
    tabs_evaluacion.add(tab_transformaciones, text="Transformaciones")
    tabs_evaluacion.add(tab_limites, text="Limites")

    texto_rut = crear_texto(tab_rut)

    panel_conicas = tk.PanedWindow(tab_conicas, orient="horizontal", bg=COLOR_SUPERFICIE, sashwidth=6)
    panel_conicas.pack(fill="both", expand=True)
    frame_texto_conicas = tk.Frame(panel_conicas, bg=COLOR_SUPERFICIE)
    frame_eval_conicas = tk.Frame(panel_conicas, bg=COLOR_SUPERFICIE)
    panel_conicas.add(frame_texto_conicas, minsize=420)
    panel_conicas.add(frame_eval_conicas, minsize=360)

    texto_conicas = crear_texto(frame_texto_conicas)
    titulo_panel(frame_eval_conicas, "Evaluacion interactiva de elementos geometricos")
    frame_campos_dinamicos = tk.Frame(frame_eval_conicas, bg=COLOR_SUPERFICIE)
    frame_campos_dinamicos.pack(fill="both", expand=True, padx=0, pady=(4, 10))

    texto_transformaciones = crear_texto(tab_transformaciones)

    frame_limites_layout = tk.PanedWindow(tab_limites, orient="horizontal", bg=COLOR_SUPERFICIE, sashwidth=6)
    frame_limites_layout.pack(fill="both", expand=True)
    frame_texto_limites = tk.Frame(frame_limites_layout, bg=COLOR_SUPERFICIE)
    frame_tabla_limites = tk.Frame(frame_limites_layout, bg=COLOR_SUPERFICIE)
    frame_limites_layout.add(frame_texto_limites, minsize=480)
    frame_limites_layout.add(frame_tabla_limites, minsize=280)

    texto_limites = crear_texto(frame_texto_limites)
    titulo_panel(frame_tabla_limites, "Evidencia computacional")
    tabla = ttk.Treeview(frame_tabla_limites, columns=("x", "y"), show="headings", height=10)
    tabla.heading("x", text="x")
    tabla.heading("y", text="f(x)")
    tabla.column("x", width=120, anchor="center")
    tabla.column("y", width=120, anchor="center")
    tabla.pack(fill="both", expand=True, padx=10, pady=10)

    escribir(texto_rut, "RUT\n====================================\nIngreso\nEsperando datos.\n\nValidacion\nPendiente.\n\nProcedimiento modulo 11\nPendiente.\n")
    escribir(texto_conicas, "CONICAS\n====================================\nEcuacion general\nPendiente.\n\nProcedimiento\nPendiente.\n\nForma canonica\nPendiente.\n\nClasificacion\nPendiente.\n\nGrafica\nPendiente.\n")
    escribir(texto_transformaciones, "TRANSFORMACIONES\n====================================\nProcedimiento\nPendiente.\n\nGrafica original\nPendiente.\n\nGrafica transformada\nPendiente.\n")
    escribir(texto_limites, "LIMITES\n====================================\nConstruccion\nPendiente.\n\nLimites laterales\nPendiente.\n\nEvidencia computacional\nPendiente.\n\nGrafica\nPendiente.\n\nConclusion\nPendiente.\n")

    mostrar_figura(tab_grafica_conica, figura_inicial("Esperando RUT"))
    mostrar_figura(tab_grafica_original, figura_inicial("Grafica original"))
    mostrar_figura(tab_grafica_transformada, figura_inicial("Grafica transformada"))
    mostrar_figura(tab_grafica_limites, figura_inicial("Limites"))

    def seleccionar(indice_eval, indice_grafica=None):
        tabs_evaluacion.select(indice_eval)
        if indice_grafica is not None:
            tabs_grafica.select(indice_grafica)

    boton_menu(panel_izq, "RUT: ingreso, validacion, modulo 11", lambda: seleccionar(tab_rut, None))
    boton_menu(panel_izq, "Conicas: ecuacion, forma, clasificacion", lambda: seleccionar(tab_conicas, tab_grafica_conica))
    boton_menu(panel_izq, "Transformaciones: original y transformada", lambda: seleccionar(tab_transformaciones, tab_grafica_original))
    boton_menu(panel_izq, "Limites: laterales y evidencia", lambda: seleccionar(tab_limites, tab_grafica_limites))

    def generar():
        rut_ingresado = entrada_rut.get().strip()

        plt.close("all")

        for item in tabla.get_children():
            tabla.delete(item)

        limpiar_frame(frame_campos_dinamicos)

        valido, detalle_rut = validar_rut_detallado(rut_ingresado)
        escribir(texto_rut, construir_reporte_rut(rut_ingresado or "(vacio)", valido, detalle_rut))

        if not rut_ingresado:
            estado_rut.config(text="Debe ingresar un RUT")
            tabs_evaluacion.select(tab_rut)
            return

        if not valido:
            estado_rut.config(text="RUT invalido")
            estado_conica.config(text="Esperando RUT valido")
            estado_limite.config(text="Esperando RUT valido")
            tabs_evaluacion.select(tab_rut)
            return

        d, dv = obtener_digitos(rut_ingresado)
        if d is None:
            estado_rut.config(text="Formato invalido")
            tabs_evaluacion.select(tab_rut)
            return

        estado_rut.config(text="Valido" if valido else "Invalido")

        v = calcular_v(dv)
        A, B, C, D, E, procedimiento_conica = construir_ecuacion_detallado(d, v)
        tipo = clasificar_conica(A, B, C, D, E)
        tipo_grafica = tipo.lower()

        escribir(texto_conicas, construir_reporte_conicas(A, B, C, D, E, procedimiento_conica, tipo))
        escribir(texto_transformaciones, construir_reporte_transformaciones(A, B, C, D, E))

        estado_conica.config(text=f"{tipo}: {ecuacion_general(A, B, C, D, E)}")
        mostrar_campos_evaluacion(frame_campos_dinamicos, tipo_grafica, A, B, C, D, E)

        fig_conica = graficar_desde_ecuacion(tipo_grafica, A, B, C, D, E)
        fig_original = graficar_desde_ecuacion(tipo_grafica, A, B, C, D, E)
        fig_transformada = graficar_desde_ecuacion(tipo_grafica, A, B, C, D, E)

        if fig_conica.axes:
            fig_conica.axes[0].set_title("Conica clasificada")
        if fig_original.axes:
            fig_original.axes[0].set_title("Grafica original: ecuacion general")
        if fig_transformada.axes:
            fig_transformada.axes[0].set_title("Grafica transformada: forma canonica")

        mostrar_figura(tab_grafica_conica, fig_conica)
        mostrar_figura(tab_grafica_original, fig_original)
        mostrar_figura(tab_grafica_transformada, fig_transformada)

        datos_funcion = construir_funcion(d)
        resultado_limites = analizar_limites(d)
        tabla_datos = obtener_tabla(datos_funcion)

        for fila in tabla_datos:
            tabla.insert("", "end", values=(fila["x"], fila["y"]))

        escribir(texto_limites, construir_reporte_limites(datos_funcion, resultado_limites, tabla_datos))
        estado_limite.config(
            text=(
                f"x = {datos_funcion['a']} | "
                f"izq: {resultado_limites['izquierda']} | "
                f"der: {resultado_limites['derecha']}"
            )
        )

        fig_limites = graficar_funcion(datos_funcion)
        mostrar_figura(tab_grafica_limites, fig_limites)

        tabs_evaluacion.select(tab_conicas)
        tabs_grafica.select(tab_grafica_conica)

    boton_generar = tk.Button(
        panel_izq,
        text="Generar proyecto",
        command=generar,
        bg=COLOR_BOTON,
        activebackground=COLOR_BOTON_HOVER,
        fg="#ffffff",
        activeforeground="#ffffff",
        font=("Arial", 12, "bold"),
        relief="flat",
        padx=16,
        pady=13,
        bd=0,
        highlightthickness=2,
        highlightbackground="#66cfc3",
        highlightcolor="#d4fff6",
        cursor="hand2",
    )
    boton_generar.pack(fill="x", padx=18, pady=(18, 8))

    entrada_rut.bind("<Return>", lambda _e: generar())

    tk.Label(
        panel_izq,
        text="MAT1186 - Proyecto EID",
        bg=COLOR_PANEL,
        fg=COLOR_MUTED,
        font=("Arial", 9),
    ).pack(side="bottom", pady=12)

    ventana.mainloop()


if __name__ == "__main__":
    iniciar_app()
