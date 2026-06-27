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

def canonica_a_general(h, k, a2, b2):

    if a2 == 0 or b2 == 0:
        raise ValueError("Los denominadores a2 y b2 no pueden ser cero.")

    A = b2
    B = a2
    C = -2 * h * b2
    D = -2 * k * a2
    E = (b2 * h ** 2) + (a2 * k ** 2) - (a2 * b2)

    return A, B, C, D, E


def procedimiento_canonica_a_general(h, k, a2, b2):

    A, B, C, D, E = canonica_a_general(h, k, a2, b2)

    texto = []

    texto.append("Forma canonica original:")
    texto.append(
        f"(x-({fmt(h)}))²/{fmt(a2)} + (y-({fmt(k)}))²/{fmt(b2)} = 1"
    )
    texto.append("")

    texto.append("1. Multiplicar cruzado por los denominadores:")
    texto.append(
        f"{fmt(b2)}(x-({fmt(h)}))² + {fmt(a2)}(y-({fmt(k)}))² = {fmt(a2 * b2)}"
    )
    texto.append("")

    texto.append("2. Desarrollar los binomios al cuadrado:")
    texto.append(
        f"{fmt(b2)}(x² - {fmt(2 * h)}x + {fmt(h ** 2)}) + "
        f"{fmt(a2)}(y² - {fmt(2 * k)}y + {fmt(k ** 2)}) = {fmt(a2 * b2)}"
    )
    texto.append("")

    texto.append("3. Distribuir, ordenar e igualar a cero:")
    texto.append(ecuacion_general(A, B, C, D, E))

    return "\n".join(texto)


def forma_canonica(A, B, C, D, E):

    texto = []

    texto.append("====================================")
    texto.append(" FORMA CANÓNICA")
    texto.append("====================================")
    texto.append("")

    if (
        (A == 0 and B == 0)
        or (A == 0 and B != 0 and C == 0)
        or (B == 0 and A != 0 and D == 0)
        or (
            A != 0
            and B != 0
            and (
                -E
                + (C ** 2) / (4 * A)
                + (D ** 2) / (4 * B)
            ) == 0
        )
    ):
        texto.append("Caso degenerado")
        texto.append("")
        texto.append(
            "No se puede obtener una forma canonica regular sin dividir por cero."
        )
        texto.append(
            "Los coeficientes no definen una circunferencia, elipse, hiperbola o parabola valida."
        )
        return "\n".join(texto)

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
    # PARÁBOLA (Corregido con desplazamientos h y k)
    # =====================================

    else:

        texto.append("Parábola")
        texto.append("")

        if A == 0:
            
            if B == 0 or C == 0:
                texto.append("Caso degenerado de parábola.")
                return "\n".join(texto)

            # Ecuación: By² + Cx + Dy + E = 0
            k = -D / (2 * B)
            p = -C / (4 * B)
            
            # ¡Aquí está la magia! Calculamos 'h' usando 'E'
            h = ((D ** 2) / (4 * B) - E) / C

            texto.append("Orientación horizontal")
            texto.append(f"Abre hacia la {'derecha' if p > 0 else 'izquierda'}")
            texto.append("")
            
            texto.append(f"Vértice (h, k) = ({fmt(h)}, {fmt(k)})")
            texto.append(f"Foco = ({fmt(h+p)}, {fmt(k)})")
            texto.append(f"Directriz: x = {fmt(h-p)}")
            texto.append("")
            
            texto.append("Forma canónica:")
            texto.append(f"(y - ({fmt(k)}))² = {fmt(4*p)}(x - ({fmt(h)}))")

        else:
            
            if A == 0 or D == 0:
                texto.append("Caso degenerado de parábola.")
                return "\n".join(texto)

            # Ecuación: Ax² + Cx + Dy + E = 0
            h = -C / (2 * A)
            p = -D / (4 * A)
            
            # ¡Aquí está la magia! Calculamos 'k' usando 'E'
            k = ((C ** 2) / (4 * A) - E) / D

            texto.append("Orientación vertical")
            texto.append(f"Abre hacia {'arriba' if p > 0 else 'abajo'}")
            texto.append("")
            
            texto.append(f"Vértice (h, k) = ({fmt(h)}, {fmt(k)})")
            texto.append(f"Foco = ({fmt(h)}, {fmt(k+p)})")
            texto.append(f"Directriz: y = {fmt(k-p)}")
            texto.append("")
            
            texto.append("Forma canónica:")
            texto.append(f"(x - ({fmt(h)}))² = {fmt(4*p)}(y - ({fmt(k)}))")

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
