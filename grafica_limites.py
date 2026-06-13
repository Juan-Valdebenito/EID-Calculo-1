import matplotlib.pyplot as plt

from funciones import evaluar_funcion


def graficar_funcion(datos):

    fig, ax = plt.subplots(figsize=(7, 5))

    a = datos["a"]

    x = []
    y = []

    inicio = a - 5
    fin = a + 5

    paso = 0.025

    valor = inicio

    while valor <= fin:

        resultado = evaluar_funcion(valor, datos)

        x.append(valor)

        if resultado is None:
            y.append(None)
        else:
            y.append(resultado)

        valor += paso

    ax.plot(x, y)

    ax.axvline(
        a,
        linestyle="--"
    )

    ax.set_title("Gráfica de la función")

    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")

    ax.grid(True)

    return fig