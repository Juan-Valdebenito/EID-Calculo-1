






def valor_absoluto(x):

    if x < 0:
        return -x

    return x


# =========================================
# CONSTRUCCION DE FUNCION
# =========================================

def construir_funcion(d):

    d1,d2,d3,d4,d5,d6,d7,d8 = d

    a = d3

    print("\n===================================")
    print(" CONSTRUCCION FUNCION POR TRAMOS ")
    print("===================================")

    print(f"\nPunto de analisis:")
    print(f"a = d3 = {a}")

    resto = d8 % 3

    # =========================================
    # CASO 1 -> REMOVIBLE
    # =========================================

    if resto == 0:

        print(f"\nd8 = {d8}")
        print(f"{d8} % 3 = 0")

        print("\nSe genera discontinuidad removible")

        print("\nFuncion:")
        print(f"f(x) = ((x-{a})(x+{d1})) / (x-{a})")

        print("\nSimplificacion manual:")
        print(f"f(x) = x + {d1}, con x ≠ {a}")

        datos = {
            "tipo": "removible",
            "a": a,
            "d1": d1
        }

        return datos

    # =========================================
    # CASO 2 -> SALTO
    # =========================================

    elif resto == 1:

        print(f"\nd8 = {d8}")
        print(f"{d8} % 3 = 1")

        print("\nSe genera discontinuidad de salto")

        print("\nFuncion:")

        print(f"""
f(x) =

x + {d2}      si x < {a}

x + {d4}      si x >= {a}
""")

        datos = {
            "tipo": "salto",
            "a": a,
            "d2": d2,
            "d4": d4
        }

        return datos

    # =========================================
    # CASO 3 -> INFINITA
    # =========================================

    else:

        print(f"\nd8 = {d8}")
        print(f"{d8} % 3 = 2")

        print("\nSe genera discontinuidad infinita")

        print("\nFuncion:")
        print(f"f(x) = ({d5}+1)/(x-{a})")

        datos = {
            "tipo": "infinita",
            "a": a,
            "numerador": d5 + 1
        }

        return datos


# =========================================
# EVALUAR FUNCION
# =========================================

def evaluar_funcion(x, datos):

    tipo = datos["tipo"]

    # =========================================
    # REMOVIBLE
    # =========================================

    if tipo == "removible":

        a = datos["a"]
        d1 = datos["d1"]

        if x == a:
            return None

        numerador = (x - a) * (x + d1)
        denominador = (x - a)

        return numerador / denominador

    # =========================================
    # SALTO
    # =========================================

    elif tipo == "salto":

        a = datos["a"]
        d2 = datos["d2"]
        d4 = datos["d4"]

        if x < a:
            return x + d2

        return x + d4

    # =========================================
    # INFINITA
    # =========================================

    elif tipo == "infinita":

        a = datos["a"]
        numerador = datos["numerador"]

        if x == a:
            return None

        return numerador / (x - a)


# =========================================
# LIMITES LATERALES
# =========================================

def limite_izquierda(datos):

    tipo = datos["tipo"]
    a = datos["a"]

    # =========================================
    # REMOVIBLE
    # =========================================

    if tipo == "removible":

        d1 = datos["d1"]

        limite = a + d1

        print("\nLimite por izquierda:")

        print(f"""
lim x→{a}⁻ ((x-{a})(x+{d1}))/(x-{a})

= lim x→{a}⁻ (x+{d1})

= {a}+{d1}

= {limite}
""")

        return limite

    # =========================================
    # SALTO
    # =========================================

    elif tipo == "salto":

        d2 = datos["d2"]

        limite = a + d2

        print("\nLimite por izquierda:")

        print(f"""
lim x→{a}⁻ (x+{d2})

= {a}+{d2}

= {limite}
""")

        return limite

    # =========================================
    # INFINITA
    # =========================================

    elif tipo == "infinita":

        numerador = datos["numerador"]

        print("\nLimite por izquierda:")

        print(f"""
lim x→{a}⁻ {numerador}/(x-{a})
""")

        if numerador > 0:

            print("El denominador se acerca a 0 negativo")

            print("Resultado → -∞")

            return "-∞"

        else:

            print("Resultado → +∞")

            return "+∞"


# =========================================
# LIMITE DERECHA
# =========================================

def limite_derecha(datos):

    tipo = datos["tipo"]
    a = datos["a"]

    # =========================================
    # REMOVIBLE
    # =========================================

    if tipo == "removible":

        d1 = datos["d1"]

        limite = a + d1

        print("\nLimite por derecha:")

        print(f"""
lim x→{a}⁺ ((x-{a})(x+{d1}))/(x-{a})

= lim x→{a}⁺ (x+{d1})

= {a}+{d1}

= {limite}
""")

        return limite

    # =========================================
    # SALTO
    # =========================================

    elif tipo == "salto":

        d4 = datos["d4"]

        limite = a + d4

        print("\nLimite por derecha:")

        print(f"""
lim x→{a}⁺ (x+{d4})

= {a}+{d4}

= {limite}
""")

        return limite

    # =========================================
    # INFINITA
    # =========================================

    elif tipo == "infinita":

        numerador = datos["numerador"]

        print("\nLimite por derecha:")

        print(f"""
lim x→{a}⁺ {numerador}/(x-{a})
""")

        if numerador > 0:

            print("El denominador se acerca a 0 positivo")

            print("Resultado → +∞")

            return "+∞"

        else:

            print("Resultado → -∞")

            return "-∞"


# =========================================
# ANALISIS COMPLETO
# =========================================

def analizar_limites(d):

    datos = construir_funcion(d)

    izquierda = limite_izquierda(datos)

    derecha = limite_derecha(datos)

    print("\n===================================")
    print(" ANALISIS FINAL ")
    print("===================================")

    print(f"\nLimite izquierda = {izquierda}")
    print(f"Limite derecha = {derecha}")

    tipo = datos["tipo"]

    # =========================================
    # REMOVIBLE
    # =========================================

    if tipo == "removible":

        print("\nLos limites laterales son iguales")

        print("El limite SI existe")

        print("La discontinuidad es removible")

    # =========================================
    # SALTO
    # =========================================

    elif tipo == "salto":

        if izquierda == derecha:

            print("\nLos limites son iguales")

            print("El limite existe")

        else:

            print("\nLos limites son distintos")

            print("El limite NO existe")

            print("Discontinuidad de salto")

    # =========================================
    # INFINITA
    # =========================================

    elif tipo == "infinita":

        print("\nLa funcion crece sin limite")

        print("Existe discontinuidad infinita")

        print(f"Asintota vertical: x = {datos['a']}")

    return datos