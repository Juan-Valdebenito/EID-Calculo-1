from funciones import evaluar_funcion


# =========================================
# FORMATO NUMERICO
# =========================================

def fmt(n):

    if n is None:
        return "No definido"

    if isinstance(n, str):
        return n

    if isinstance(n, float):

        texto = str(round(n, 6))
        texto = texto.rstrip("0").rstrip(".")

        return texto

    return str(n)


# =========================================
# TABLA DE VALORES
# =========================================

def obtener_tabla(datos):

    a = datos["a"]

    valores = [
        a - 1,
        a - 0.1,
        a - 0.01,
        a - 0.001,
        a,
        a + 0.001,
        a + 0.01,
        a + 0.1,
        a + 1
    ]

    tabla = []

    for x in valores:

        y = evaluar_funcion(x, datos)

        tabla.append({
            "x": fmt(x),
            "y": fmt(y)
        })

    return tabla


# =========================================
# EXPLICACION DETALLADA
# =========================================

def generar_evidencia_texto(datos):

    a = datos["a"]

    texto = ""

    texto += "===================================\n"
    texto += "EVIDENCIA COMPUTACIONAL\n"
    texto += "===================================\n\n"

    texto += f"Punto crítico: a = {a}\n\n"

    tabla = obtener_tabla(datos)

    texto += f"{'x':<15}{'f(x)':<20}\n"
    texto += "-" * 35 + "\n"

    for fila in tabla:
        texto += f"{fila['x']:<15}{fila['y']:<20}\n"

    texto += "\n"

    tipo = datos["tipo"]

    if tipo == "removible":

        texto += (
            "Interpretación:\n"
            "Los valores de la tabla se aproximan al mismo número\n"
            "por ambos lados del punto crítico.\n\n"
            "La función no está definida en x = a,\n"
            "pero el límite sí existe.\n\n"
            "Conclusión:\n"
            "Discontinuidad removible.\n"
        )

    elif tipo == "salto":

        texto += (
            "Interpretación:\n"
            "Los valores por izquierda y derecha se aproximan\n"
            "a números distintos.\n\n"
            "Conclusión:\n"
            "Discontinuidad de salto.\n"
            "El límite no existe.\n"
        )

    elif tipo == "infinita":

        texto += (
            "Interpretación:\n"
            "Los valores crecen o decrecen sin límite\n"
            "al acercarse al punto crítico.\n\n"
            f"Asíntota vertical: x = {a}\n\n"
            "Conclusión:\n"
            "Discontinuidad infinita.\n"
        )

    elif tipo == "continua":
        texto += (
            "Interpretación:\n"
            "Los valores de la tabla se aproximan exactamente al mismo número\n"
            "tanto por la izquierda como por la derecha del punto crítico.\n\n"
            "Además, la función está definida en x = a y coincide con dicho límite.\n\n"
            "Conclusión:\n"
            "La función es continua en todo su dominio.\n"
        )

    return texto


# =========================================
# VERSION CONSOLA
# =========================================

def tabla_valores(datos):

    print(generar_evidencia_texto(datos))