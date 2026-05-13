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


def graficar_conica(tipo, datos):
    print("\nDATOS RECIBIDOS:")
    print("Tipo:", tipo)
    print(datos)

    fig, ax = plt.subplots()

    puntos_x = []
    puntos_y = []

    # =========================
    # CIRCUNFERENCIA / ELIPSE
    # =========================

    if tipo == "circunferencia" or tipo == "elipse":

        h = datos["h"]
        k = datos["k"]
        a2 = datos["a2"]
        b2 = datos["b2"]

        inicio = h - raiz_aproximada(a2)
        fin = h + raiz_aproximada(a2)

        x = inicio

        while x <= fin:

            parte = 1 - ((x - h) ** 2) / a2

            if parte >= 0:

                y = raiz_aproximada(parte * b2)

                puntos_x.append(x)
                puntos_y.append(k + y)

                puntos_x.append(x)
                puntos_y.append(k - y)

            x += 0.1

    # =========================
    # HIPÉRBOLA
    # =========================

    elif tipo == "hipérbola":

        h = datos["h"]
        k = datos["k"]
        a2 = datos["a2"]
        b2 = datos["b2"]
        orientacion = datos["orientacion"]

        t = -20

        while t <= 20:

            # HIPÉRBOLA HORIZONTAL

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

            # HIPÉRBOLA VERTICAL

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

    # =========================
    # PARÁBOLA
    # =========================

    elif tipo == "parábola":

        h = datos["h"]
        k = datos["k"]
        p = datos["p"]
        orientacion = datos["orientacion"]

        t = -20

        while t <= 20:

            # PARÁBOLA VERTICAL

            if orientacion == "vertical":

                x = h + t

                y = k + (t ** 2) / (4 * p)

                puntos_x.append(x)
                puntos_y.append(y)

            # PARÁBOLA HORIZONTAL

            else:

                y = k + t

                x = h + (t ** 2) / (4 * p)

                puntos_x.append(x)
                puntos_y.append(y)

            t += 0.05

    # =========================

    ax.plot(puntos_x, puntos_y, marker='.')

    ax.axhline(0)
    ax.axvline(0)

    ax.set_title(f"Gráfica de la {tipo}")

    ax.grid(True)

    ax.set_aspect('equal')

    plt.show()


def graficar_desde_ecuacion(tipo, A, B, C, D, E):

    # =========================
    # CIRCUNFERENCIA / ELIPSE
    # =========================

    if tipo == "circunferencia" or tipo == "elipse":

        h = -C / (2 * A)
        k = -D / (2 * B)

        constante = -E + (C ** 2) / (4 * A) + (D ** 2) / (4 * B)

        a2 = constante / A
        b2 = constante / B

        datos = {
            "h": h,
            "k": k,
            "a2": valor_absoluto(a2),
            "b2": valor_absoluto(b2)
        }

        graficar_conica(tipo, datos)

    # =========================
    # HIPÉRBOLA
    # =========================

    elif tipo == "hipérbola":

        h = -C / (2 * A)
        k = -D / (2 * B)

        constante = -E + (C ** 2) / (4 * A) + (D ** 2) / (4 * B)

        if constante == 0:

            print("No se puede graficar.")
            return

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

        graficar_conica(tipo, datos)

    # =========================
    # PARÁBOLA
    # =========================

    elif tipo == "parábola":

    # PARÁBOLA HORIZONTAL

        if A == 0:

            k = -D / (2 * B)

            h = 0

            p = -C / (4 * B)

            datos = {
                "h": h,
                "k": k,
                "p": p,
                "orientacion": "horizontal"
            }

        # PARÁBOLA VERTICAL

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

        graficar_conica(tipo, datos)
