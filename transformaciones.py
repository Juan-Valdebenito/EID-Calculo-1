def es_cero(n):
    return abs(n) < 0.0000001


def fmt(n):
    if es_cero(n):
        n = 0

    if isinstance(n, float) and n.is_integer():
        return str(int(n))

    texto = str(round(n, 6))
    texto = texto.rstrip("0").rstrip(".")
    return texto


def termino(coeficiente, variable):
    if es_cero(coeficiente):
        return None

    signo = "+" if coeficiente > 0 else "-"
    valor = abs(coeficiente)

    if variable != "" and abs(valor - 1) < 0.0000001:
        cuerpo = variable
    elif variable == "":
        cuerpo = fmt(valor)
    else:
        cuerpo = f"{fmt(valor)}{variable}"

    return signo, cuerpo


def ecuacion_general(A, B, C, D, E):
    datos = [
        (A, "x²"),
        (B, "y²"),
        (C, "x"),
        (D, "y"),
        (E, "")
    ]

    terminos = []

    for coeficiente, variable in datos:
        t = termino(coeficiente, variable)
        if t is not None:
            terminos.append(t)

    if len(terminos) == 0:
        return "0 = 0"

    signo, cuerpo = terminos[0]

    if signo == "-":
        texto = f"-{cuerpo}"
    else:
        texto = cuerpo

    for signo, cuerpo in terminos[1:]:
        texto += f" {signo} {cuerpo}"

    return texto + " = 0"


def binomio(variable, centro):
    if es_cero(centro):
        return variable

    if centro > 0:
        return f"({variable} - {fmt(centro)})"

    return f"({variable} + {fmt(abs(centro))})"


def forma_canonica(A, B, C, D, E, mostrar_elementos=True):
    print("Ecuación general recibida:")
    print(ecuacion_general(A, B, C, D, E))

    if es_cero(A) and not es_cero(B):
        parabola_horizontal(B, C, D, E, mostrar_elementos)

    elif es_cero(B) and not es_cero(A):
        parabola_vertical(A, C, D, E, mostrar_elementos)

    elif not es_cero(A) and not es_cero(B):
        conica_central(A, B, C, D, E, mostrar_elementos)

    else:
        print("No se puede transformar: A y B son ambos cero.")


def parabola_horizontal(B, C, D, E, mostrar_elementos=True):
    print("\nComo A = 0 y B ≠ 0, la cónica es una parábola horizontal.")
    print("Forma general:")
    print(ecuacion_general(0, B, C, D, E))

    k = -D / (2 * B)

    print("\nCompletamos cuadrado en y:")
    print(f"k = -D/(2B) = -({fmt(D)}) / (2·{fmt(B)}) = {fmt(k)}")

    constante = E - B * (k ** 2)

    print("\nReescritura:")
    print(f"{fmt(B)}{binomio('y', k)}² + ({fmt(C)})x + {fmt(constante)} = 0")

    h = -constante / C
    cuatro_p = -C / B
    p = cuatro_p / 4

    print("\nDespejamos a forma canónica:")
    print(f"{binomio('y', k)}² = {fmt(cuatro_p)}{binomio('x', h)}")

    if mostrar_elementos:
        print("\nElementos principales:")
        print(f"Vértice: V({fmt(h)}, {fmt(k)})")
        print(f"4p = {fmt(cuatro_p)}")
        print(f"p = {fmt(p)}")
        print(f"Foco: F({fmt(h + p)}, {fmt(k)})")
        print(f"Directriz: x = {fmt(h - p)}")

        if p > 0:
            print("La parábola abre hacia la derecha.")
        else:
            print("La parábola abre hacia la izquierda.")


def parabola_vertical(A, C, D, E, mostrar_elementos=True):
    print("\nComo B = 0 y A ≠ 0, la cónica es una parábola vertical.")
    print("Forma general:")
    print(ecuacion_general(A, 0, C, D, E))

    h = -C / (2 * A)

    print("\nCompletamos cuadrado en x:")
    print(f"h = -C/(2A) = -({fmt(C)}) / (2·{fmt(A)}) = {fmt(h)}")

    constante = E - A * (h ** 2)

    print("\nReescritura:")
    print(f"{fmt(A)}{binomio('x', h)}² + ({fmt(D)})y + {fmt(constante)} = 0")

    k = -constante / D
    cuatro_p = -D / A
    p = cuatro_p / 4

    print("\nDespejamos a forma canónica:")
    print(f"{binomio('x', h)}² = {fmt(cuatro_p)}{binomio('y', k)}")

    if mostrar_elementos:
        print("\nElementos principales:")
        print(f"Vértice: V({fmt(h)}, {fmt(k)})")
        print(f"4p = {fmt(cuatro_p)}")
        print(f"p = {fmt(p)}")
        print(f"Foco: F({fmt(h)}, {fmt(k + p)})")
        print(f"Directriz: y = {fmt(k - p)}")

        if p > 0:
            print("La parábola abre hacia arriba.")
        else:
            print("La parábola abre hacia abajo.")


def conica_central(A, B, C, D, E, mostrar_elementos=True):
    print("\nComo A ≠ 0 y B ≠ 0, completamos cuadrados en x e y.")

    h = -C / (2 * A)
    k = -D / (2 * B)

    print(f"h = -C/(2A) = -({fmt(C)}) / (2·{fmt(A)}) = {fmt(h)}")
    print(f"k = -D/(2B) = -({fmt(D)}) / (2·{fmt(B)}) = {fmt(k)}")

    constante = E - A * (h ** 2) - B * (k ** 2)

    print("\nReescritura:")
    print(f"{fmt(A)}{binomio('x', h)}² + {fmt(B)}{binomio('y', k)}² + {fmt(constante)} = 0")

    lado_derecho = -constante

    print("\nPasamos la constante al otro lado:")
    print(f"{fmt(A)}{binomio('x', h)}² + {fmt(B)}{binomio('y', k)}² = {fmt(lado_derecho)}")

    if es_cero(A - B):
        radio_cuadrado = lado_derecho / A

        print("\nForma canónica de circunferencia:")
        print(f"{binomio('x', h)}² + {binomio('y', k)}² = {fmt(radio_cuadrado)}")

        if mostrar_elementos:
            print("\nElementos principales:")
            print(f"Centro: C({fmt(h)}, {fmt(k)})")
            print(f"Radio² = {fmt(radio_cuadrado)}")

    elif A * B > 0:
        denom_x = lado_derecho / A
        denom_y = lado_derecho / B

        print("\nForma canónica de elipse:")
        print(f"{binomio('x', h)}²/{fmt(denom_x)} + {binomio('y', k)}²/{fmt(denom_y)} = 1")

        if mostrar_elementos:
            print("\nElementos principales:")
            print(f"Centro: C({fmt(h)}, {fmt(k)})")
            print(f"Denominador bajo x: {fmt(denom_x)}")
            print(f"Denominador bajo y: {fmt(denom_y)}")

    else:
        denom_x = lado_derecho / A
        denom_y = lado_derecho / B

        print("\nForma canónica de hipérbola:")

        if denom_x > 0:
            print(f"{binomio('x', h)}²/{fmt(denom_x)} - {binomio('y', k)}²/{fmt(abs(denom_y))} = 1")
        else:
            print(f"{binomio('y', k)}²/{fmt(denom_y)} - {binomio('x', h)}²/{fmt(abs(denom_x))} = 1")

        if mostrar_elementos:
            print("\nElementos principales:")
            print(f"Centro: C({fmt(h)}, {fmt(k)})")
            print(f"Denominador bajo x: {fmt(abs(denom_x))}")
            print(f"Denominador bajo y: {fmt(abs(denom_y))}")