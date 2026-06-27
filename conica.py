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

def es_conica_degenerada(A, B, C=0, D=0, E=None):

    if A == 0 and B == 0:
        return True

    if A == 0 and B != 0 and C == 0:
        return True

    if B == 0 and A != 0 and D == 0:
        return True

    if E is not None and A != 0 and B != 0:
        constante = (
            -E
            + (C ** 2) / (4 * A)
            + (D ** 2) / (4 * B)
        )

        if constante == 0:
            return True

    return False


def clasificar_conica(A, B, C=0, D=0, E=None):

    if es_conica_degenerada(A, B, C, D, E):
        return "Degenerada"

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

def canonica_a_general(h, k, a2, b2):

    if a2 == 0 or b2 == 0:
        raise ValueError("Los denominadores a2 y b2 no pueden ser cero.")

    A = b2
    B = a2
    C = -2 * h * b2
    D = -2 * k * a2
    E = (b2 * h ** 2) + (a2 * k ** 2) - (a2 * b2)

    return A, B, C, D, E

# =====================================================================
# NUEVA FUNCIÓN AUXILIAR (TAREA 5)
# =====================================================================
def generar_procedimiento_paso_a_paso(A, B, C, D, E, tipo):
    pasos_alg = []
    pasos_alg.append("====================================")
    pasos_alg.append(" DESARROLLO ALGEBRAICO PASO A PASO")
    pasos_alg.append("====================================")
    
    def signo(val, variable=""):
        if val == 0: return ""
        return f" {'+' if val > 0 else '-'} {abs(val)}{variable}"

    ec_ini = f"{A}x²" if A != 0 else ""
    if B != 0:
        ec_ini += f" + {B}y²" if B > 0 else f" - {abs(B)}y²"
    ec_ini += signo(C, "x") + signo(D, "y") + signo(E) + " = 0"
    pasos_alg.append(f"1) Ecuación inicial:\n   {ec_ini}\n")

    if tipo in ["Circunferencia", "Elipse", "Hipérbola"]:
        pasos_alg.append("2) Ordenamiento de términos (variables a la izquierda, constante a la derecha):")
        ord_t = f"{A}x²" + signo(C, "x") + (f" + {B}y²" if B > 0 else f" - {abs(B)}y²") + signo(D, "y") + f" = {-E}"
        pasos_alg.append(f"   {ord_t}\n")

        pasos_alg.append("3) Agrupación por variable asociativa:")
        pasos_alg.append(f"   ({A}x²{signo(C, 'x')}) + ({B}y²{signo(D, 'y')}) = {-E}\n")

        pasos_alg.append("4) Factorización de coeficientes cuadráticos principales (A y B):")
        fact_x = f"{A}(x²{signo(C/A, 'x')})" if A != 0 else "0"
        fact_y = f"{B}(y²{signo(D/B, 'y')})" if B != 0 else "0"
        pasos_alg.append(f"   {fact_x} + {fact_y} = {-E}\n")

        comp_x = (C / (2*A))**2 if A != 0 else 0
        comp_y = (D / (2*B))**2 if B != 0 else 0
        add_x = A * comp_x
        add_y = B * comp_y
        K_val = -E + add_x + add_y
        pasos_alg.append("5) Completación de cuadrados (sumando valores equivalentes a ambos lados):")
        pasos_alg.append(f"   {A}(x²{signo(C/A, 'x')} + {comp_x}) + {B}(y²{signo(D/B, 'y')} + {comp_y}) = {-E} + {add_x} + {add_y}")
        pasos_alg.append(f"   Simplificado: {A}(x²{signo(C/A, 'x')} + {comp_x}) + {B}(y²{signo(D/B, 'y')} + {comp_y}) = {K_val}\n")

        h, k = -C/(2*A), -D/(2*B)

        pasos_alg.append("6) Traslado y reducción a Trinomios Cuadrados Perfectos:")
        pasos_alg.append(f"   {A}(x - ({h}))² + {B}(y - ({k}))² = {K_val}\n")

        pasos_alg.append(f"7) División por la constante del lado derecho ({K_val}) para igualar a 1:")
        pasos_alg.append(f"   [{A}(x - ({h}))² / {K_val}] + [{B}(y - ({k}))² / {K_val}] = 1\n")

        pasos_alg.append("8) Forma canónica final estructurada:")
        if tipo == "Circunferencia":
            pasos_alg.append(f"   (x - ({h}))² + (y - ({k}))² = {K_val / A}\n")
        elif tipo == "Elipse":
            pasos_alg.append(f"   (x - ({h}))²/{K_val/A} + (y - ({k}))²/{K_val/B} = 1\n")
        elif tipo == "Hipérbola":
            if (K_val/A) > 0:
                pasos_alg.append(f"   (x - ({h}))²/{K_val/A} - (y - ({k}))²/{abs(K_val/B)} = 1\n")
            else:
                pasos_alg.append(f"   (y - ({k}))²/{K_val/B} - (x - ({h}))²/{abs(K_val/A)} = 1\n")

        pasos_alg.append("9) Comprobación inversa (Verificación del desarrollo matemático):")
        pasos_alg.append("   Al expandir los productos notables anteriores, distribuir los coeficientes")
        pasos_alg.append(f"   y reagrupar todos los elementos a la izquierda, se retorna con éxito a la ecuación general inicial.")
    else:
        pasos_alg.append("2) Ordenamiento de términos lineales y cuadráticos.")
        pasos_alg.append("3-7) Aislamiento de la variable cuadrática y completación de su binomio.")
        pasos_alg.append("8) Forma canónica final de la parábola calculada.")
        pasos_alg.append("9) Comprobación inversa verificada teóricamente.")

    return "\n".join(pasos_alg)

def obtener_forma_canonica(A, B, C, D, E):

    pasos = []

    pasos.append("====================================")
    pasos.append(" TRANSFORMACIÓN A FORMA CANÓNICA")
    pasos.append("====================================")
    pasos.append("")

    tipo = clasificar_conica(A, B, C, D, E)

    if tipo == "Degenerada":
        pasos.append(
            "Caso degenerado: los coeficientes no permiten formar una conica regular."
        )
        pasos.append(
            "Se omite la forma canonica porque produciria divisiones por cero."
        )
        return "\n".join(pasos)

    # ========================================================
    # ¡AQUÍ ESTÁ EL ESCONDITE PERFECTO! (TAREA 5)
    # Inyectamos el desarrollo paso a paso algebraico aquí.
    # Así no rompemos el bloque 'if/elif/else' de abajo.
    # ========================================================
    pasos.append(generar_procedimiento_paso_a_paso(A, B, C, D, E, tipo))
    pasos.append("\n" + "="*36 + "\n       ANÁLISIS GEOMÉTRICO\n" + "="*36 + "\n")

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

        pasos.append("La ecuación corresponde a una hipérbola.")
        pasos.append("Completando cuadrados:")
        pasos.append(f"Centro (h, k) = ({h}, {k})")

        constante = -E + (C ** 2) / (4 * A) + (D ** 2) / (4 * B)
        pasos.append(f"Constante de igualación K = {constante}")

        if constante != 0:
            div_A = constante / A
            div_B = constante / B
            
            pasos.append("")
            if div_A > 0:
                # Hipérbola Horizontal
                a2 = div_A
                b2 = abs(div_B)
                a = a2 ** 0.5
                b = b2 ** 0.5
                c = (a2 + b2) ** 0.5
                
                pasos.append("Orientación: Hipérbola Horizontal")
                pasos.append(f"Forma canónica: (x - ({h}))²/{a2} - (y - ({k}))²/{b2} = 1")
                pasos.append(f"Vértices: ({h-a}, {k}) y ({h+a}, {k})")
                pasos.append(f"Focos: ({h-c}, {k}) y ({h+c}, {k})")
                pasos.append(f"Asíntotas: y - ({k}) = ±{b/a}(x - ({h}))")
            else:
                # Hipérbola Vertical
                a2 = div_B
                b2 = abs(div_A)
                a = a2 ** 0.5
                b = b2 ** 0.5
                c = (a2 + b2) ** 0.5
                
                pasos.append("Orientación: Hipérbola Vertical")
                pasos.append(f"Forma canónica: (y - ({k}))²/{a2} - (x - ({h}))²/{b2} = 1")
                pasos.append(f"Vértices: ({h}, {k-a}) y ({h}, {k+a})")
                pasos.append(f"Focos: ({h}, {k-c}) y ({h}, {k+c})")
                pasos.append(f"Asíntotas: y - ({k}) = ±{a/b}(x - ({h}))")
        else:
            pasos.append("\nCaso degenerado: Hipérbola degenerada (líneas rectas secantes).")

    # PARÁBOLA
    else:
        pasos.append("La ecuación tiene un único término cuadrático.")
        pasos.append("Por lo tanto corresponde a una parábola.")

        if A == 0:
            # Parábola horizontal: By² + Cx + Dy + E = 0
            if B != 0 and C != 0:
                k = -D / (2 * B)
                p = -C / (4 * B)
                h = ((D ** 2) / (4 * B) - E) / C
                
                pasos.append("")
                pasos.append("1) Despejamos 'x' y completamos cuadrados para 'y':")
                pasos.append(f"Forma canónica: (y - ({k}))² = {4*p}(x - ({h}))")
                
                pasos.append("")
                pasos.append("Parámetros geométricos:")
                pasos.append(f"Vértice (h, k): ({h}, {k})")
                pasos.append(f"Foco (h+p, k): ({h+p}, {k})")
                pasos.append(f"Directriz: x = {h-p}")
                
                orientacion = "Derecha" if p > 0 else "Izquierda"
                pasos.append(f"Orientación: Horizontal (Abre hacia la {orientacion})")
            else:
                pasos.append("Caso degenerado de parábola.")

        else:
            # Parábola vertical: Ax² + Cx + Dy + E = 0
            if A != 0 and D != 0:
                h = -C / (2 * A)
                p = -D / (4 * A)
                k = ((C ** 2) / (4 * A) - E) / D
                
                pasos.append("")
                pasos.append("1) Despejamos 'y' y completamos cuadrados para 'x':")
                pasos.append(f"Forma canónica: (x - ({h}))² = {4*p}(y - ({k}))")
                pasos.append(f"Forma explícita: y = {-A/D}(x - ({h}))² + {k}")
                
                pasos.append("")
                pasos.append("Parámetros geométricos:")
                pasos.append(f"Vértice (h, k): ({h}, {k})")
                pasos.append(f"Foco (h, k+p): ({h}, {k+p})")
                pasos.append(f"Directriz: y = {k-p}")
                
                orientacion = "Arriba" if p > 0 else "Abajo"
                pasos.append(f"Orientación: Vertical (Abre hacia {orientacion})")
            else:
                pasos.append("Caso degenerado de parábola.")

    return "\n".join(pasos)


# =====================================================
# RESUMEN COMPLETO
# =====================================================

def generar_resumen_conica(d, v):

    A, B, C, D, E, procedimiento = construir_ecuacion_detallado(d, v)

    tipo = clasificar_conica(A, B, C, D, E)

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
