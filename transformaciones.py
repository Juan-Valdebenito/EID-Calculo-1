# =====================================================
# FORMATEO DE NÚMEROS
# =====================================================

def fmt(valor):

    if int(valor) == valor:
        return str(int(valor))

    return str(round(valor, 2))


# =====================================================
# ECUACIÓN GENERAL
# =====================================================

def ecuacion_general(A, B, C, D, E):

    texto = ""

    # ==========================
    # Término x²
    # ==========================

    if A != 0:
        texto += f"{fmt(A)}x² "

    # ==========================
    # Término y²
    # ==========================

    if B > 0:

        if texto == "":
            texto += f"{fmt(B)}y² "
        else:
            texto += f"+ {fmt(B)}y² "

    elif B < 0:

        if texto == "":
            texto += f"- {fmt(abs(B))}y² "
        else:
            texto += f"- {fmt(abs(B))}y² "

    # ==========================
    # Término x
    # ==========================

    if C > 0:

        if texto == "":
            texto += f"{fmt(C)}x "
        else:
            texto += f"+ {fmt(C)}x "

    elif C < 0:

        if texto == "":
            texto += f"- {fmt(abs(C))}x "
        else:
            texto += f"- {fmt(abs(C))}x "

    # ==========================
    # Término y
    # ==========================

    if D > 0:

        if texto == "":
            texto += f"{fmt(D)}y "
        else:
            texto += f"+ {fmt(D)}y "

    elif D < 0:

        if texto == "":
            texto += f"- {fmt(abs(D))}y "
        else:
            texto += f"- {fmt(abs(D))}y "

    # ==========================
    # Constante
    # ==========================

    if E > 0:

        if texto == "":
            texto += f"{fmt(E)} "
        else:
            texto += f"+ {fmt(E)} "

    elif E < 0:

        if texto == "":
            texto += f"- {fmt(abs(E))} "
        else:
            texto += f"- {fmt(abs(E))} "

    texto += "= 0"

    return texto

# =====================================================
# FORMA CANÓNICA
# =====================================================

def forma_canonica(A, B, C, D, E):

    texto = []

    texto.append("====================================")
    texto.append(" FORMA CANÓNICA")
    texto.append("====================================")
    texto.append("")

    # =====================================
    # CIRCUNFERENCIA / ELIPSE
    # =====================================

    if A != 0 and B != 0 and A * B > 0:

        h = -C / (2 * A)
        k = -D / (2 * B)

        constante = (
            -E
            + (C ** 2) / (4 * A)
            + (D ** 2) / (4 * B)
        )

        texto.append("Completando cuadrados:")
        texto.append("")

        texto.append(f"Centro = ({fmt(h)}, {fmt(k)})")
        texto.append("")

        if A == B:

            radio2 = constante / A

            if radio2 > 0:

                radio = radio2 ** 0.5

                texto.append("Circunferencia")
                texto.append("")

                texto.append(
                    f"(x-{fmt(h)})² + (y-{fmt(k)})² = {fmt(radio2)}"
                )

                texto.append("")
                texto.append(f"Radio = {fmt(radio)}")

        else:

            a2 = abs(constante / A)
            b2 = abs(constante / B)

            texto.append("Elipse")
            texto.append("")

            texto.append(
                f"(x-{fmt(h)})²/{fmt(a2)} + (y-{fmt(k)})²/{fmt(b2)} = 1"
            )

            texto.append("")
            texto.append(f"a² = {fmt(a2)}")
            texto.append(f"b² = {fmt(b2)}")

    # =====================================
    # HIPÉRBOLA
    # =====================================

    elif A != 0 and B != 0 and A * B < 0:

        h = -C / (2 * A)
        k = -D / (2 * B)

        constante = (
            -E
            + (C ** 2) / (4 * A)
            + (D ** 2) / (4 * B)
        )

        a2 = abs(constante / A)
        b2 = abs(constante / B)

        texto.append("Hipérbola")
        texto.append("")

        texto.append(f"Centro = ({fmt(h)}, {fmt(k)})")
        texto.append("")

        texto.append(
            f"(x-{fmt(h)})²/{fmt(a2)} - (y-{fmt(k)})²/{fmt(b2)} = 1"
        )

        texto.append("")
        texto.append(f"a² = {fmt(a2)}")
        texto.append(f"b² = {fmt(b2)}")

    # =====================================
    # PARÁBOLA
    # =====================================

    else:

        texto.append("Parábola")
        texto.append("")

        if A == 0:

            k = -D / (2 * B)

            texto.append(
                "Orientación horizontal"
            )

            texto.append("")
            texto.append(
                f"Vértice aproximado = (0 , {fmt(k)})"
            )

        else:

            h = -C / (2 * A)

            texto.append(
                "Orientación vertical"
            )

            texto.append("")
            texto.append(
                f"Vértice aproximado = ({fmt(h)} , 0)"
            )

    return "\n".join(texto)


# =====================================================
# CENTRO DE LA CÓNICA
# =====================================================

def obtener_centro(A, B, C, D):

    if A == 0 or B == 0:
        return None

    h = -C / (2 * A)
    k = -D / (2 * B)

    return (h, k)


# =====================================================
# RESUMEN COMPLETO
# =====================================================

def resumen_transformacion(A, B, C, D, E):

    texto = []

    texto.append("====================================")
    texto.append(" ECUACIÓN GENERAL")
    texto.append("====================================")
    texto.append("")

    texto.append(
        ecuacion_general(A, B, C, D, E)
    )

    texto.append("")
    texto.append(
        forma_canonica(A, B, C, D, E)
    )

    return "\n".join(texto)