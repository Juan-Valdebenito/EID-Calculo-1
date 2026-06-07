import matplotlib.pyplot as plt
import numpy as np

from funciones import evaluar_funcion


def graficar_funcion(datos):

    fig, ax = plt.subplots(figsize=(7, 5))

    a = datos["a"]

    x = np.linspace(a - 5, a + 5, 400)

    y = []

    for valor in x:

        resultado = evaluar_funcion(valor, datos)

        if resultado is None:
            y.append(np.nan)
        else:
            y.append(resultado)

    ax.plot(x, y)

    ax.axvline(
        a,
        linestyle="--"
    )

    ax.set_title("Gráfica de la función")

    ax.grid(True)

    return fig