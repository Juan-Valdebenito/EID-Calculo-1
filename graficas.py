import matplotlib.pyplot as plt


def valor_absoluto(x):

    if x < 0:
        return -x

    return x


def raiz_aproximada(n):

    if n < 0:
        return None

    if n == 0:
        return 0

    x = n

    for _ in range(20):
        x = (x + n / x) / 2

    return x


# =====================================================
# GRAFICAR CONICA
# =====================================================

def graficar_conica(tipo, datos):

    fig, ax = plt.subplots(figsize=(7, 7))

    puntos_x = []
    puntos_y = []

    # =================================================
    # CIRCUNFERENCIA / ELIPSE
    # =================================================

    if tipo == "circunferencia" or tipo == "elipse":

        h = datos["h"]
        k = datos["k"]
        a2 = datos["a2"]
        b2 = datos["b2"]

        if a2 <= 0 or b2 <= 0:
            return fig

        inicio = h - raiz_aproximada(a2)
        fin = h + raiz_aproximada(a2)

        x = inicio

        while x <= fin:

            parte = 1 - ((x - h) ** 2) / a2

            if parte >= 0:

                y = raiz_aproximada(parte * b2)

                if y is not None:

                    puntos_x.append(x)
                    puntos_y.append(k + y)

                    puntos_x.append(x)
                    puntos_y.append(k - y)

            x += 0.1

    # =================================================
    # HIPERBOLA
    # =================================================

    elif tipo == "hipérbola":

        h = datos["h"]
        k = datos["k"]
        a2 = datos["a2"]
        b2 = datos["b2"]
        orientacion = datos["orientacion"]

        if a2 <= 0 or b2 <= 0:
            return fig

        t = -20

        while t <= 20:

            # HIPERBOLA HORIZONTAL

            if orientacion == "horizontal":

                x = h + t

                parte = ((x - h) ** 2) / a2 - 1

                if parte >= 0:

                    y = raiz_aproximada(parte * b2)

                    if y is not None:

                        puntos_x.append(x)
                        puntos_y.append(k + y)

                        puntos_x.append(x)
                        puntos_y.append(k - y)

            # HIPERBOLA VERTICAL

            else:

                y = k + t

                parte = ((y - k) ** 2) / a2 - 1

                if parte >= 0:

                    x = raiz_aproximada(parte * b2)

                    if x is not None:

                        puntos_x.append(h + x)
                        puntos_y.append(y)

                        puntos_x.append(h - x)
                        puntos_y.append(y)

            t += 0.05

    # =================================================
    # PARABOLA
    # =================================================

    elif tipo == "parábola":

        h = datos["h"]
        k = datos["k"]
        p = datos["p"]
        orientacion = datos["orientacion"]

        if p == 0:
            return fig

        t = -20

        while t <= 20:

            # PARABOLA VERTICAL

            if orientacion == "vertical":

                x = h + t

                y = k + (t ** 2) / (4 * p)

                puntos_x.append(x)
                puntos_y.append(y)

            # PARABOLA HORIZONTAL

            else:

                y = k + t

                x = h + (t ** 2) / (4 * p)

                puntos_x.append(x)
                puntos_y.append(y)

            t += 0.05

    # =================================================
    # DIBUJAR
    # =================================================

    ax.plot(
        puntos_x,
        puntos_y,
        marker='.',
        linestyle='',
        markersize=2
    )

    ax.axhline(0)

    ax.axvline(0)

    ax.set_title(f"Gráfica de la {tipo}")

    ax.grid(True)

    ax.set_aspect('equal')

    return fig


# =====================================================
# GRAFICAR DESDE ECUACION
# =====================================================

def graficar_desde_ecuacion(tipo, A, B, C, D, E):

    # =================================================
    # CIRCUNFERENCIA / ELIPSE
    # =================================================

    if tipo == "circunferencia" or tipo == "elipse":

        if A == 0 or B == 0:
            return None

        h = -C / (2 * A)

        k = -D / (2 * B)

        constante = (
            -E
            + (C ** 2) / (4 * A)
            + (D ** 2) / (4 * B)
        )

        a2 = constante / A

        b2 = constante / B

        datos = {
            "h": h,
            "k": k,
            "a2": valor_absoluto(a2),
            "b2": valor_absoluto(b2)
        }

        return graficar_conica(tipo, datos)

    # =================================================
    # HIPERBOLA
    # =================================================

    elif tipo == "hipérbola":

        if A == 0 or B == 0:
            return None

        h = -C / (2 * A)

        k = -D / (2 * B)

        constante = (
            -E
            + (C ** 2) / (4 * A)
            + (D ** 2) / (4 * B)
        )

        if constante == 0:

            return None

        a2 = valor_absoluto(constante / A)

        b2 = valor_absoluto(constante / B)

        if A > 0:
            orientacion = "horizontal"

        else:
            orientacion = "vertical"

        datos = {
            "h": h,
            "k": k,
            "a2": a2,
            "b2": b2,
            "orientacion": orientacion
        }

        return graficar_conica(tipo, datos)

    # =================================================
    # PARABOLA
    # =================================================

    elif tipo == "parábola":

        # PARABOLA HORIZONTAL

        if A == 0:

            if B == 0:
                return None

            k = -D / (2 * B)

            h = 0

            p = -C / (4 * B)

            datos = {
                "h": h,
                "k": k,
                "p": p,
                "orientacion": "horizontal"
            }

        # PARABOLA VERTICAL

        else:

            h = -C / (2 * A)

            k = 0

            p = -D / (4 * A)

            datos = {
                "h": h,
                "k": k,
                "p": p,
                "orientacion": "vertical"
            }

        return graficar_conica(tipo, datos)

    return None