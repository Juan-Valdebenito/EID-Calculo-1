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

    # =========================================
    # CAMBIO DE SIGNO
    # =========================================

    if d8 % 2 != 0:

        procedimiento.append(
            f"d8 = {d8} es impar → B cambia signo"
        )

        B = -B

        procedimiento.append(f"B = {B}")

        procedimiento.append("")

    # =========================================
    # CIRCUNFERENCIA
    # =========================================

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

    # =========================================
    # PARÁBOLA
    # =========================================

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

    # =========================================
    # RESTO DE COEFICIENTES
    # =========================================

    C = -(d5 + d6)
    D = -(d7 + d8)
    E = d1 + d3 + d5 + d7

    procedimiento.append(f"C = -({d5}+{d6}) = {C}")
    procedimiento.append(f"D = -({d7}+{d8}) = {D}")
    procedimiento.append(f"E = {d1}+{d3}+{d5}+{d7} = {E}")

    texto_procedimiento = "\n".join(procedimiento)

    return A, B, C, D, E, texto_procedimiento


# =====================================================
# CLASIFICACIÓN DE LA CÓNICA
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
# ECUACIÓN EN FORMATO LEGIBLE
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

    resumen = []

    resumen.append(procedimiento)

    resumen.append("")
    resumen.append("====================================")
    resumen.append(" RESULTADO")
    resumen.append("====================================")
    resumen.append("")

    resumen.append(f"Ecuación:")
    resumen.append(ecuacion)

    resumen.append("")
    resumen.append(f"Tipo de cónica: {tipo}")

    return "\n".join(resumen)