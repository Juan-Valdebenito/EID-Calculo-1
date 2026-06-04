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

    ax.axhline(0, color='black', linewidth=0.8)
    ax.axvline(0, color='black', linewidth=0.8)
    ax.set_title(f"Gráfica de la {tipo.capitalize()}")
    ax.grid(True, linestyle='--', alpha=0.7)

    # =================================================
    # CIRCUNFERENCIA / ELIPSE 
    # =================================================

    if tipo == "circunferencia" or tipo == "elipse":
        h, k, a2, b2 = datos["h"], datos["k"], datos["a2"], datos["b2"]

        if a2 <= 0 or b2 <= 0:
            return fig

        inicio = h - raiz_aproximada(a2)
        fin = h + raiz_aproximada(a2)

        x_arriba, y_arriba = [], []
        x_abajo, y_abajo = [], []
        x = inicio

        while x <= fin:
            parte = 1 - ((x - h) ** 2) / a2
            if parte >= 0:
                y = raiz_aproximada(parte * b2)
                if y is not None:
                    x_arriba.append(x)
                    y_arriba.append(k + y)

                    x_abajo.insert(0, x)
                    y_abajo.insert(0, k - y)
            x += 0.02

        puntos_x = x_arriba + x_abajo + [x_arriba[0]]
        puntos_y = y_arriba + y_abajo + [y_arriba[0]]

        color_conica = 'blue' if tipo == "circunferencia" else 'purple'
        ax.plot(puntos_x, puntos_y, color=color_conica, linestyle='-', linewidth=2)
        ax.set_aspect('equal')

    # =================================================
    # HIPERBOLA 
    # =================================================

    elif tipo == "hipérbola":
        h, k, a2, b2 = datos["h"], datos["k"], datos["a2"], datos["b2"]
        orientacion = datos["orientacion"]

        if a2 <= 0 or b2 <= 0:
            return fig

        a = raiz_aproximada(a2)
        b = raiz_aproximada(b2)
        
        # Limitamos el dibujo a 15 unidades desde el vértice para que el zoom sea perfecto
        rango_dibujo = 15  
        paso = 0.1

        if orientacion == "horizontal":
            x = h + a
            x_der, y_der_arriba, y_der_abajo = [], [], []
            while x <= h + a + rango_dibujo:
                parte = ((x - h)**2) / a2 - 1
                if parte >= 0:
                    y = raiz_aproximada(parte * b2)
                    x_der.append(x)
                    y_der_arriba.append(k + y)
                    y_der_abajo.append(k - y)
                x += paso
            
            rama_1_x = list(reversed(x_der)) + x_der
            rama_1_y = list(reversed(y_der_abajo)) + y_der_arriba
            
            x = h - a
            x_izq, y_izq_arriba, y_izq_abajo = [], [], []
            while x >= h - a - rango_dibujo: 
                parte = ((x - h)**2) / a2 - 1
                if parte >= 0:
                    y = raiz_aproximada(parte * b2)
                    x_izq.append(x)
                    y_izq_arriba.append(k + y)
                    y_izq_abajo.append(k - y)
                x -= paso

            rama_2_x = list(reversed(x_izq)) + x_izq
            rama_2_y = list(reversed(y_izq_abajo)) + y_izq_arriba
            
            pendiente = b / a
            lim_x_min = h - a - rango_dibujo
            lim_x_max = h + a + rango_dibujo

            asintota_1_x = [lim_x_min, lim_x_max]
            asintota_1_y = [pendiente * (lim_x_min - h) + k, pendiente * (lim_x_max - h) + k]
            
            asintota_2_x = [lim_x_min, lim_x_max]
            asintota_2_y = [-pendiente * (lim_x_min - h) + k, -pendiente * (lim_x_max - h) + k]

        else: 
            y = k + a
            y_arr, x_arr_der, x_arr_izq = [], [], []
            while y <= k + a + rango_dibujo:
                parte = ((y - k)**2) / a2 - 1
                if parte >= 0:
                    x_val = raiz_aproximada(parte * b2)
                    y_arr.append(y)
                    x_arr_der.append(h + x_val)
                    x_arr_izq.append(h - x_val)
                y += paso
                
            rama_1_y = list(reversed(y_arr)) + y_arr
            rama_1_x = list(reversed(x_arr_izq)) + x_arr_der

            y = k - a
            y_aba, x_aba_der, x_aba_izq = [], [], []
            while y >= k - a - rango_dibujo:
                parte = ((y - k)**2) / a2 - 1
                if parte >= 0:
                    x_val = raiz_aproximada(parte * b2)
                    y_aba.append(y)
                    x_aba_der.append(h + x_val)
                    x_aba_izq.append(h - x_val)
                y -= paso
                
            rama_2_y = list(reversed(y_aba)) + y_aba
            rama_2_x = list(reversed(x_aba_izq)) + x_aba_der
            
            pendiente = a / b 
            lim_y_min = k - a - rango_dibujo
            lim_y_max = k + a + rango_dibujo
            
            asintota_1_x = [(lim_y_min - k) / pendiente + h, (lim_y_max - k) / pendiente + h]
            asintota_1_y = [lim_y_min, lim_y_max]
            
            asintota_2_x = [(lim_y_min - k) / (-pendiente) + h, (lim_y_max - k) / (-pendiente) + h]
            asintota_2_y = [lim_y_min, lim_y_max]


        ax.plot(rama_1_x, rama_1_y, color='red', linestyle='-', linewidth=2)
        ax.plot(rama_2_x, rama_2_y, color='red', linestyle='-', linewidth=2)
        
        ax.plot(asintota_1_x, asintota_1_y, color='gray', linestyle='--', linewidth=1.5, alpha=0.6)
        ax.plot(asintota_2_x, asintota_2_y, color='gray', linestyle='--', linewidth=1.5, alpha=0.6)
        
        ax.set_aspect('auto')

    # =================================================
    # PARABOLA 
    # =================================================

    elif tipo == "parábola":
        h, k, p, orientacion = datos["h"], datos["k"], datos["p"], datos["orientacion"]

        if p == 0:
            return fig

        puntos_x, puntos_y = [], []
        t = -20

        while t <= 20:
            if orientacion == "vertical":
                puntos_x.append(h + t)
                puntos_y.append(k + (t ** 2) / (4 * p))
            else:
                puntos_y.append(k + t)
                puntos_x.append(h + (t ** 2) / (4 * p))
            t += 0.1

        ax.plot(puntos_x, puntos_y, color='green', linestyle='-', linewidth=2)
        ax.set_aspect('auto') 

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