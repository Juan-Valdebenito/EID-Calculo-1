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

        constante = (
            -E
            + (C**2)/(4*A)
            + (D**2)/(4*B)
        )

        a2 = abs(constante / A)
        b2 = abs(constante / B)

        a = np.sqrt(a2)
        b = np.sqrt(b2)

        if a == 0 or b == 0:
            mostrar_caso_degenerado(ax)
            ax.set_xlim(-20,20)
            ax.set_ylim(-20,20)
            return fig

        ax.plot(
            h,
            k,
            marker="o"
        )

        ax.annotate(
            f"Centro ({round(h,2)}, {round(k,2)})",
            (h, k)
        )

        x = np.linspace(
            h - 20,
            h + 20,
            4000
        )

        if A > 0:

            parte = ((x-h)**2)/a2 - 1

            y1 = []
            y2 = []

            for valor in parte:

                if valor >= 0:

                    y = np.sqrt(valor*b2)

                    y1.append(k+y)
                    y2.append(k-y)

                else:

                    y1.append(np.nan)
                    y2.append(np.nan)

            ax.plot(x, y1)
            ax.plot(x, y2)

            # Asíntotas

            m = b/a

            xa = np.array([h-20, h+20])

            ax.plot(
                xa,
                m*(xa-h)+k,
                linestyle="--"
            )

            ax.plot(
                xa,
                -m*(xa-h)+k,
                linestyle="--"
            )

        else:

            y = np.linspace(
                k-20,
                k+20,
                4000
            )

            parte = ((y-k)**2)/a2 - 1

            x1 = []
            x2 = []

            for valor in parte:

                if valor >= 0:

                    xx = np.sqrt(valor*b2)

                    x1.append(h+xx)
                    x2.append(h-xx)

                else:

                    x1.append(np.nan)
                    x2.append(np.nan)

            ax.plot(x1, y)
            ax.plot(x2, y)

        ax.set_aspect("equal")

    # =========================================
    # PARÁBOLA
    # =========================================

    elif tipo == "parábola":

        if A == 0:

            if B == 0 or C == 0:
                mostrar_caso_degenerado(ax)
                ax.set_xlim(-20,20)
                ax.set_ylim(-20,20)
                return fig

            k = -D/(2*B)

            p = -C/(4*B)

            if p == 0:
                mostrar_caso_degenerado(ax)
                ax.set_xlim(-20,20)
                ax.set_ylim(-20,20)
                return fig

            t = np.linspace(-20,20,1000)

            x = (t**2)/(4*p)
            y = t + k

            ax.plot(x,y)

            foco = (p,k)

            ax.plot(
                foco[0],
                foco[1],
                marker="x"
            )

            ax.annotate(
                "Foco",
                foco
            )

            ax.axvline(
                -p,
                linestyle="--"
            )

        else:

            if A == 0 or D == 0:
                mostrar_caso_degenerado(ax)
                ax.set_xlim(-20,20)
                ax.set_ylim(-20,20)
                return fig

            h = -C/(2*A)

            p = -D/(4*A)

            if p == 0:
                mostrar_caso_degenerado(ax)
                ax.set_xlim(-20,20)
                ax.set_ylim(-20,20)
                return fig

            t = np.linspace(-20,20,1000)

            x = t + h
            y = (t**2)/(4*p)

            ax.plot(x,y)

            foco = (h,p)

            ax.plot(
                foco[0],
                foco[1],
                marker="x"
            )

            ax.annotate(
                "Foco",
                foco
            )

            ax.axhline(
                -p,
                linestyle="--"
            )

    ax.set_xlim(-20,20)
    ax.set_ylim(-20,20)

    return fig
