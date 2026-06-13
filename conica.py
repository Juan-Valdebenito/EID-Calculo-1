# =====================================================
# CONSTRUCCIÓN DE LA ECUACIÓN DE LA CÓNICA
# =====================================================

def construir_ecuacion_detallado(d, v):

    d1, d2, d3, d4, d5, d6, d7, d8 = d

    procedimiento = []

    procedimiento.append("====================================")
    procedimiento.append(" CONSTRUCCIÓN DE LA ECUACIÓN")
    procedimiento.append("====================================")
    procedimiento.append("")

    procedimiento.append(f"A = ({d1}+{d2})/{v}")
    A = (d1 + d2) / v
    procedimiento.append(f"A = {A}")

    procedimiento.append("")

    procedimiento.append(f"B = ({d3}+{d4})/{v}")
    B = (d3 + d4) / v
    procedimiento.append(f"B = {B}")

    procedimiento.append("")

    if d8 % 2 != 0:

        procedimiento.append(
            f"d8 = {d8} es impar → B cambia signo"
        )

        B = -B

        procedimiento.append(f"B = {B}")
        procedimiento.append("")

    if d1 == d2:

        procedimiento.append(
            f"d1 = d2 = {d1}"
        )

        procedimiento.append(
            "Se fuerza A = B"
        )

        B = A

        procedimiento.append(f"B = {B}")
        procedimiento.append("")

    if (d5 + d6) % 3 == 0:

        procedimiento.append(
            f"(d5+d6) = {d5+d6}"
        )

        procedimiento.append(
            f"{d5+d6} % 3 = 0"
        )

        if d7 % 2 == 0:

            procedimiento.append(
                "d7 es par → Parábola Vertical"
            )

            B = 0

        else:

            procedimiento.append(
                "d7 es impar → Parábola Horizontal"
            )

            A = 0

        procedimiento.append("")

    C = -(d5 + d6)
    D = -(d7 + d8)
    E = d1 + d3 + d5 + d7

    procedimiento.append(f"C = -({d5}+{d6}) = {C}")
    procedimiento.append(f"D = -({d7}+{d8}) = {D}")
    procedimiento.append(f"E = {d1}+{d3}+{d5}+{d7} = {E}")

    texto_procedimiento = "\n".join(procedimiento)

    return A, B, C, D, E, texto_procedimiento


# =====================================================
# CLASIFICACIÓN
# =====================================================

def clasificar_conica(A, B):

    if A == B and A != 0:
        return "Circunferencia"

    elif A * B > 0:
        return "Elipse"

    elif A * B < 0:
        return "Hipérbola"

    else:
        return "Parábola"


# =====================================================
# ECUACIÓN GENERAL
# =====================================================

def obtener_ecuacion_general(A, B, C, D, E):

    ecuacion = ""

    if A != 0:
        ecuacion += f"{A}x² "

    if B > 0:
        ecuacion += f"+ {B}y² "
    elif B < 0:
        ecuacion += f"- {abs(B)}y² "

    if C > 0:
        ecuacion += f"+ {C}x "
    elif C < 0:
        ecuacion += f"- {abs(C)}x "

    if D > 0:
        ecuacion += f"+ {D}y "
    elif D < 0:
        ecuacion += f"- {abs(D)}y "

    if E > 0:
        ecuacion += f"+ {E}"
    elif E < 0:
        ecuacion += f"- {abs(E)}"

    ecuacion += " = 0"

    return ecuacion


# =====================================================
# FORMA CANÓNICA DETALLADA
# =====================================================

def obtener_forma_canonica(A, B, C, D, E):

    pasos = []

    pasos.append("====================================")
    pasos.append(" TRANSFORMACIÓN A FORMA CANÓNICA")
    pasos.append("====================================")
    pasos.append("")

    tipo = clasificar_conica(A, B)

    # CIRCUNFERENCIA Y ELIPSE

    if tipo in ["Circunferencia", "Elipse"]:

        h = -C / (2 * A)
        k = -D / (2 * B)

        pasos.append("Completando cuadrados:")
        pasos.append("")

        pasos.append(f"h = -({C})/(2·{A}) = {h}")
        pasos.append(f"k = -({D})/(2·{B}) = {k}")

        constante = (
            -E
            + (C ** 2) / (4 * A)
            + (D ** 2) / (4 * B)
        )

        pasos.append("")
        pasos.append("Constante de la forma canónica:")
        pasos.append(f"K = {constante}")

        if tipo == "Circunferencia":

            radio2 = constante / A

            pasos.append("")
            pasos.append("Forma canónica:")

            pasos.append(
                f"(x - ({h}))² + (y - ({k}))² = {radio2}"
            )

        else:

            a2 = constante / A
            b2 = constante / B

            pasos.append("")
            pasos.append("Forma canónica:")

            pasos.append(
                f"(x - ({h}))²/{a2} + (y - ({k}))²/{b2} = 1"
            )

    # HIPÉRBOLA

    elif tipo == "Hipérbola":

        h = -C / (2 * A)
        k = -D / (2 * B)

        pasos.append("Completando cuadrados:")
        pasos.append("")

        pasos.append(f"h = {h}")
        pasos.append(f"k = {k}")

        constante = (
            -E
            + (C ** 2) / (4 * A)
            + (D ** 2) / (4 * B)
        )

        pasos.append("")
        pasos.append(f"K = {constante}")

        pasos.append("")
        pasos.append(
            "La ecuación corresponde a una hipérbola."
        )

    # PARÁBOLA

    else:

        pasos.append(
            "La ecuación tiene un único término cuadrático."
        )

        pasos.append(
            "Por lo tanto corresponde a una parábola."
        )

        if A == 0:

            pasos.append("")
            pasos.append(
                "Parábola horizontal."
            )

        else:

            pasos.append("")
            pasos.append(
                "Parábola vertical."
            )

    return "\n".join(pasos)


# =====================================================
# RESUMEN COMPLETO
# =====================================================

def generar_resumen_conica(d, v):

    A, B, C, D, E, procedimiento = construir_ecuacion_detallado(d, v)

    tipo = clasificar_conica(A, B)

    ecuacion = obtener_ecuacion_general(
        A,
        B,
        C,
        D,
        E
    )

    forma_canonica = obtener_forma_canonica(
        A,
        B,
        C,
        D,
        E
    )

    resumen = []

    resumen.append(procedimiento)

    resumen.append("")
    resumen.append("====================================")
    resumen.append(" RESULTADO")
    resumen.append("====================================")
    resumen.append("")

    resumen.append("Ecuación General:")
    resumen.append(ecuacion)

    resumen.append("")

    resumen.append(f"Tipo de cónica: {tipo}")

    resumen.append("")
    resumen.append(forma_canonica)

    return "\n".join(resumen)