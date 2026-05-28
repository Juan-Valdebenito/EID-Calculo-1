



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

def tabla_valores(datos):

    a = datos["a"]

    print("\n===================================")
    print(" EVIDENCIA COMPUTACIONAL ")
    print("===================================")

    print(f"\nPunto critico: a = {a}")

    print("\nTabla de aproximacion:\n")

    print(f"{'x':<15}{'f(x)':<20}")

    print("-" * 35)

    # =========================================
    # VALORES IZQUIERDA
    # =========================================

    izquierda = [
        a - 1,
        a - 0.1,
        a - 0.01,
        a - 0.001
    ]

    # =========================================
    # VALORES DERECHA
    # =========================================

    derecha = [
        a + 0.001,
        a + 0.01,
        a + 0.1,
        a + 1
    ]

    # =========================================
    # MOSTRAR IZQUIERDA
    # =========================================

    print("\n--- Aproximacion por izquierda ---\n")

    for x in izquierda:

        y = evaluar_funcion(x, datos)

        print(f"{fmt(x):<15}{fmt(y):<20}")

    # =========================================
    # PUNTO EXACTO
    # =========================================

    print("\n--- Punto critico ---\n")

    y = evaluar_funcion(a, datos)

    print(f"{fmt(a):<15}{fmt(y):<20}")

    # =========================================
    # MOSTRAR DERECHA
    # =========================================

    print("\n--- Aproximacion por derecha ---\n")

    for x in derecha:

        y = evaluar_funcion(x, datos)

        print(f"{fmt(x):<15}{fmt(y):<20}")

    # =========================================
    # INTERPRETACION
    # =========================================

    print("\n===================================")
    print(" INTERPRETACION ")
    print("===================================")

    tipo = datos["tipo"]

    # =========================================
    # REMOVIBLE
    # =========================================

    if tipo == "removible":

        print("\nLos valores se acercan al mismo numero")

        print("La funcion NO esta definida en x = a")

        print("Existe discontinuidad removible")

    # =========================================
    # SALTO
    # =========================================

    elif tipo == "salto":

        print("\nLos valores izquierdos y derechos")

        print("se acercan a numeros distintos")

        print("Existe discontinuidad de salto")

    # =========================================
    # INFINITA
    # =========================================

    elif tipo == "infinita":

        print("\nLos valores crecen o decrecen")

        print("sin limite cerca de x = a")

        print("Existe discontinuidad infinita")

        print(f"Asintota vertical: x = {a}")


# =========================================
# TABLA EN FORMATO LISTA
# (UTIL PARA INTERFAZ GRAFICA)
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

        fila = {
            "x": fmt(x),
            "y": fmt(y)
        }

        tabla.append(fila)

    return tabla