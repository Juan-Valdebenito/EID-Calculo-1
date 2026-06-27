import matplotlib.pyplot as plt
import numpy as np


# =====================================================
# UTILIDADES
# =====================================================

def valor_absoluto(x):

    if x < 0:
        return -x

    return x


def mostrar_caso_degenerado(ax):

    ax.text(
        0.5,
        0.5,
        "Caso degenerado\nNo hay conica regular para graficar",
        transform=ax.transAxes,
        ha="center",
        va="center",
        fontsize=12,
    )


# =====================================================
# GRAFICAR DESDE ECUACIÓN
# =====================================================

def graficar_desde_ecuacion(tipo, A, B, C, D, E):

    fig, ax = plt.subplots(figsize=(7, 7))

    ax.axhline(0, color="black", linewidth=0.8)
    ax.axvline(0, color="black", linewidth=0.8)

    ax.grid(True)

    ax.set_title(f"{tipo.capitalize()}")

    if tipo == "degenerada":
        mostrar_caso_degenerado(ax)
        ax.set_xlim(-20,20)
        ax.set_ylim(-20,20)
        return fig

    # =========================================
    # CIRCUNFERENCIA
    # =========================================

    if tipo == "circunferencia":

        h = -C / (2 * A)
        k = -D / (2 * B)

        constante = (
            -E
            + (C**2)/(4*A)
            + (D**2)/(4*B)
        )

        radio2 = constante / A

        if radio2 <= 0:
            return fig

        radio = np.sqrt(radio2)

        t = np.linspace(0, 2*np.pi, 500)

        x = h + radio*np.cos(t)
        y = k + radio*np.sin(t)

        ax.plot(x, y, linewidth=2)

        # Centro

        ax.plot(
            h,
            k,
            marker="o",
            markersize=8
        )

        ax.annotate(
            f"Centro ({round(h,2)}, {round(k,2)})",
            (h, k)
        )

        ax.set_aspect("equal")

    # =========================================
    # ELIPSE
    # =========================================

    elif tipo == "elipse":

        h = -C / (2*A)
        k = -D / (2*B)

        constante = (
            -E
            + (C**2)/(4*A)
            + (D**2)/(4*B)
        )

        a2 = abs(constante / A)
        b2 = abs(constante / B)

        a = np.sqrt(a2)
        b = np.sqrt(b2)

        t = np.linspace(0, 2*np.pi, 500)

        x = h + a*np.cos(t)
        y = k + b*np.sin(t)

        ax.plot(x, y, linewidth=2)

        ax.plot(h, k, marker="o")

        ax.annotate(
            f"Centro ({round(h,2)}, {round(k,2)})",
            (h, k)
        )

        # Focos

        if a >= b:

            c = np.sqrt(a*a - b*b)

            foco1 = (h-c, k)
            foco2 = (h+c, k)

        else:

            c = np.sqrt(b*b - a*a)

            foco1 = (h, k-c)
            foco2 = (h, k+c)

        ax.plot(foco1[0], foco1[1], marker="x")
        ax.plot(foco2[0], foco2[1], marker="x")

        ax.annotate("F1", foco1)
        ax.annotate("F2", foco2)

        ax.set_aspect("equal")

    # =========================================
    # HIPÉRBOLA
    # =========================================

    elif tipo == "hipérbola":

        h = -C/(2*A)
        k = -D/(2*B)

        K = (C**2)/(4*A) + (D**2)/(4*B) - E

        if K == 0:
            mostrar_caso_degenerado(ax)
            ax.set_xlim(-20,20)
            ax.set_ylim(-20,20)
            return fig

        div_A = K / A
        div_B = K / B
        
        t = np.linspace(-2.5, 2.5, 500)
        
        # --- HIPÉRBOLA HORIZONTAL ---
        if div_A > 0:
            a = np.sqrt(div_A)
            b = np.sqrt(abs(div_B))
            
            # Ramas
            x_der = h + a * np.cosh(t)
            y_der = k + b * np.sinh(t)
            x_izq = h - a * np.cosh(t)
            y_izq = k + b * np.sinh(t)
            
            ax.plot(x_der, y_der, color="blue")
            ax.plot(x_izq, y_izq, color="blue")

            # Asíntotas
            x_asint = np.linspace(h - 20, h + 20, 100)
            ax.plot(x_asint, (b/a)*(x_asint - h) + k, color="red", linestyle="--", alpha=0.6)
            ax.plot(x_asint, -(b/a)*(x_asint - h) + k, color="red", linestyle="--", alpha=0.6)
            
            # Vértices y Focos
            c = np.sqrt(a**2 + b**2)
            ax.plot([h-a, h+a], [k, k], 'o', color="blue", markersize=4)
            ax.plot([h-c, h+c], [k, k], 'x', color="black", markersize=6)

        # --- HIPÉRBOLA VERTICAL ---
        else:
            a = np.sqrt(div_B)
            b = np.sqrt(abs(div_A))
            
            # Ramas (Se invierten el cosh y sinh hacia el eje Y)
            x_sup = h + b * np.sinh(t)
            y_sup = k + a * np.cosh(t)
            x_inf = h + b * np.sinh(t)
            y_inf = k - a * np.cosh(t)
            
            ax.plot(x_sup, y_sup, color="blue")
            ax.plot(x_inf, y_inf, color="blue")

            # Asíntotas
            x_asint = np.linspace(h - 20, h + 20, 100)
            ax.plot(x_asint, (a/b)*(x_asint - h) + k, color="red", linestyle="--", alpha=0.6)
            ax.plot(x_asint, -(a/b)*(x_asint - h) + k, color="red", linestyle="--", alpha=0.6)

            # Vértices y Focos
            c = np.sqrt(a**2 + b**2)
            ax.plot([h, h], [k-a, k+a], 'o', color="blue", markersize=4)
            ax.plot([h, h], [k-c, k+c], 'x', color="black", markersize=6)

        # Centro
        ax.plot(h, k, marker="+", color="black", markersize=8)

    # =========================================
    # PARÁBOLA
    # =========================================

    elif tipo == "parábola":

        if A == 0:
            # Parábola Horizontal
            if B == 0 or C == 0:
                mostrar_caso_degenerado(ax)
                ax.set_xlim(-20,20)
                ax.set_ylim(-20,20)
                return fig

            k = -D/(2*B)
            p = -C/(4*B)
            
            h = ((D**2)/(4*B) - E) / C

            if p == 0:
                mostrar_caso_degenerado(ax)
                ax.set_xlim(-20,20)
                ax.set_ylim(-20,20)
                return fig

            t = np.linspace(-20,20,1000)

            x = (t**2)/(4*p) + h
            y = t + k

            ax.plot(x,y)

            foco = (h + p, k)

            ax.plot(foco[0], foco[1], marker="x")
            ax.annotate("Foco", foco)

            ax.axvline(h - p, linestyle="--")

        else:
            # Parábola Vertical
            if A == 0 or D == 0:
                mostrar_caso_degenerado(ax)
                ax.set_xlim(-20,20)
                ax.set_ylim(-20,20)
                return fig

            h = -C/(2*A)
            p = -D/(4*A)
            
            k = ((C**2)/(4*A) - E) / D

            if p == 0:
                mostrar_caso_degenerado(ax)
                ax.set_xlim(-20,20)
                ax.set_ylim(-20,20)
                return fig

            t = np.linspace(-20,20,1000)

            x = t + h
            y = (t**2)/(4*p) + k

            ax.plot(x,y)

            foco = (h, k + p)

            ax.plot(foco[0], foco[1], marker="x")
            ax.annotate("Foco", foco)

            ax.axhline(k - p, linestyle="--")

    ax.set_xlim(-20,20)
    ax.set_ylim(-20,20)

    return fig