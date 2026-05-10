from rut import validar_rut_detallado, obtener_digitos, calcular_v
from conica import construir_ecuacion_detallado, clasificar_conica
from transformaciones import forma_canonica, ecuacion_general
#from funciones import construir_funcion, analizar_limites
#from evidencia import tabla_valores

def main():
    rut = input("Ingrese RUT: ")

    valido = validar_rut_detallado(rut)
    if not valido:
        print(" RUT invalido")
        return

    d, dv = obtener_digitos(rut)
    v = calcular_v(dv)

    print("\n=== CONSTRUCCION DE ECUACION ===")
    A, B, C, D, E = construir_ecuacion_detallado(d, v)

    print("\nEcuación general:")
    print(ecuacion_general(A, B, C, D, E))

    tipo = clasificar_conica(A, B)
    print(f"\nTipo de conica: {tipo}")

    print("\n=== FORMA CANONICA ===")
    forma_canonica(A, B, C, D, E, mostrar_elementos=False)

    # print("\n=== FUNCION POR TRAMOS ===")
    # construir_funcion(d)

    # print("\n=== LIMITES ===")
    # analizar_limites(d)

    # print("\n=== EVIDENCIA COMPUTACIONAL ===")
    # tabla_valores(d)


if __name__ == "__main__":
    main()