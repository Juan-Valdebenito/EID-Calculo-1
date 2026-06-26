# =====================================================
# UTILIDADES
# =====================================================

def valor_absoluto(x):

    if x < 0:
        return -x

    return x


# =====================================================
# CONSTRUCCION DE FUNCION
# =====================================================

def construir_funcion(d):

    d1, d2, d3, d4, d5, d6, d7, d8 = d

    a = d3

    resto = d8 % 3

    procedimiento = []

    procedimiento.append("===================================")
    procedimiento.append("CONSTRUCCION DE LA FUNCION")
    procedimiento.append("===================================")
    procedimiento.append("")
    procedimiento.append(f"d3 = {d3}")
    procedimiento.append(f"a = d3 = {a}")
    procedimiento.append("")
    procedimiento.append(f"d8 = {d8}")
    procedimiento.append(f"{d8} % 3 = {resto}")
    procedimiento.append("")

    # =================================================
    # REMOVIBLE
    # =================================================

    if resto == 0:

        procedimiento.append(
            "Como d8 es multiplo de 3 se genera una discontinuidad removible."
        )

        procedimiento.append("")
        procedimiento.append(
            f"f(x)=((x-{a})(x+{d1}))/(x-{a})"
        )

        procedimiento.append("")
        procedimiento.append("Simplificacion manual:")
        procedimiento.append(
            f"f(x)=x+{d1}, con x ≠ {a}"
        )

        return {
            "tipo": "removible",
            "a": a,
            "d1": d1,
            "funcion": f"((x-{a})(x+{d1}))/(x-{a})",
            "regla": f"{d8}%3 = 0",
            "procedimiento": "\n".join(procedimiento)
        }

    # =================================================
    # SALTO O CONTINUA
    # =================================================

    elif resto == 1:
        
        if d2 == d4:
            procedimiento.append(
                f"Como d8 % 3 = 1, pero d2 = d4 = {d2}, ambos tramos son idénticos."
            )
            procedimiento.append(
                "Por lo tanto, los límites laterales coincidirán y la función es CONTINUA."
            )
            tipo_funcion = "continua"
        else:
            procedimiento.append(
                f"Como d8 % 3 = 1 y d2 != d4 ({d2} != {d4}), se genera una discontinuidad de salto."
            )
            tipo_funcion = "salto"

        procedimiento.append("")
        procedimiento.append(f"f(x) = x + {d2}   si x < {a}")
        procedimiento.append(f"f(x) = x + {d4}   si x >= {a}")

        datos = {
            "tipo": tipo_funcion,  # Guardará "continua" o "salto" dinámicamente
            "a": a,
            "d2": d2,
            "d4": d4,
            "procedimiento": "\n".join(procedimiento)
        }
        return datos

    # =================================================
    # INFINITA
    # =================================================

    else:

        procedimiento.append(
            "Como d8 deja residuo 2 se genera una discontinuidad infinita."
        )

        procedimiento.append("")
        procedimiento.append(
            f"f(x)=({d5+1})/(x-{a})"
        )

        return {
            "tipo": "infinita",
            "a": a,
            "numerador": d5 + 1,
            "funcion": f"({d5+1})/(x-{a})",
            "regla": f"{d8}%3 = 2",
            "procedimiento": "\n".join(procedimiento)
        }


# =====================================================
# EVALUAR FUNCION
# =====================================================

def evaluar_funcion(x, datos):

    tipo = datos["tipo"]

    # ==============================================
    # REMOVIBLE
    # ==============================================

    if tipo == "removible":

        a = datos["a"]
        d1 = datos["d1"]

        if x == a:
            return None

        numerador = (x - a) * (x + d1)
        denominador = (x - a)

        return numerador / denominador

    # ==============================================
    # SALTO O CONTINUA
    # ==============================================

    elif tipo == "salto" or tipo == "continua":

        a = datos["a"]

        if x < a:
            return x + datos["d2"]

        return x + datos["d4"]

    # ==============================================
    # INFINITA
    # ==============================================

    elif tipo == "infinita":

        a = datos["a"]

        if x == a:
            return None

        return datos["numerador"] / (x - a)

    return None


# =====================================================
# LIMITE IZQUIERDA
# =====================================================

def limite_izquierda(datos):

    tipo = datos["tipo"]
    a = datos["a"]

    if tipo == "removible":

        return a + datos["d1"]

    elif tipo == "salto" or tipo == "continua":

        return a + datos["d2"]

    elif tipo == "infinita":

        if datos["numerador"] > 0:
            return "-∞"

        return "+∞"


# =====================================================
# LIMITE DERECHA
# =====================================================

def limite_derecha(datos):

    tipo = datos["tipo"]
    a = datos["a"]

    if tipo == "removible":

        return a + datos["d1"]

    elif tipo == "salto" or tipo == "continua":

        return a + datos["d4"]

    elif tipo == "infinita":

        if datos["numerador"] > 0:
            return "+∞"

        return "-∞"


# =====================================================
# VALOR FUNCION
# =====================================================

def valor_funcion_en_punto(datos):

    a = datos["a"]

    return evaluar_funcion(a, datos)


# =====================================================
# EXISTE LIMITE
# =====================================================

def existe_limite(datos):

    izquierda = limite_izquierda(datos)
    derecha = limite_derecha(datos)

    return izquierda == derecha


# =====================================================
# CONTINUIDAD
# =====================================================

def es_continua(datos):

    limite = existe_limite(datos)

    valor = valor_funcion_en_punto(datos)

    if not limite:
        return False

    if valor is None:
        return False

    return valor == limite_izquierda(datos)


# =====================================================
# JUSTIFICACION MATEMATICA
# =====================================================

def justificar(datos):

    tipo = datos["tipo"]

    izq = limite_izquierda(datos)
    der = limite_derecha(datos)

    texto = []

    texto.append("===================================")
    texto.append("JUSTIFICACION MATEMATICA")
    texto.append("===================================")
    texto.append("")

    if tipo == "continua":

        texto.append(
            f"Limite izquierdo = {izq}"
        )

        texto.append(
            f"Limite derecho = {der}"
        )

        texto.append("")

        texto.append(
            "Los limites laterales son perfectamente iguales."
        )

        texto.append(
            "Por lo tanto el limite existe."
        )

        texto.append(
            f"El valor de la funcion en el punto f(a) existe y es igual a {valor_funcion_en_punto(datos)}."
        )

        texto.append(
            "Resultado: La funcion es CONTINUA en el punto critico."
        )

    elif tipo == "removible":

        texto.append(
            f"Limite izquierdo = {izq}"
        )

        texto.append(
            f"Limite derecho = {der}"
        )

        texto.append("")

        texto.append(
            "Los limites laterales son iguales."
        )

        texto.append(
            "Por lo tanto el limite existe."
        )

        texto.append(
            "La funcion no esta definida en el punto."
        )

        texto.append(
            "Corresponde a una discontinuidad removible."
        )

    elif tipo == "salto":

        texto.append(
            f"Limite izquierdo = {izq}"
        )

        texto.append(
            f"Limite derecho = {der}"
        )

        texto.append("")

        texto.append(
            "Los limites laterales son distintos."
        )

        texto.append(
            "Por lo tanto el limite no existe."
        )

        texto.append(
            "Corresponde a una discontinuidad de salto."
        )

    else:

        texto.append(
            f"Limite izquierdo = {izq}"
        )

        texto.append(
            f"Limite derecho = {der}"
        )

        texto.append("")

        texto.append(
            "La funcion diverge al infinito."
        )

        texto.append(
            "Existe una asintota vertical."
        )

        texto.append(
            "Corresponde a una discontinuidad infinita."
        )

    return "\n".join(texto)


# =====================================================
# ANALISIS COMPLETO
# =====================================================

def analizar_limites(d):

    datos = construir_funcion(d)

    return {
        "datos": datos,
        "izquierda": limite_izquierda(datos),
        "derecha": limite_derecha(datos),
        "valor_funcion": valor_funcion_en_punto(datos),
        "existe_limite": existe_limite(datos),
        "continua": es_continua(datos),
        "justificacion": justificar(datos)
    }