def construir_ecuacion_detallado(d, v):
    d1,d2,d3,d4,d5,d6,d7,d8 = d

    print(f"A = ({d1}+{d2})/{v}")
    A = (d1 + d2) / v

    print(f"B = ({d3}+{d4})/{v}")
    B = (d3 + d4) / v

    if d8 % 2 != 0:
        print("d8 impar → B cambia signo")
        B = -B

    if d1 == d2:
        print("d1=d2 → circunferencia")
        B = A

    if (d5 + d6) % 3 == 0:
        if d7 % 2 == 0:
            print("Parábola vertical")
            B = 0
        else:
            print("Parábola horizontal")
            A = 0

    C = -(d5 + d6)
    D = -(d7 + d8)
    E = d1 + d3 + d5 + d7

    return A, B, C, D, E


def clasificar_conica(A, B):
    if A == B and A != 0:
        return "Circunferencia"
    elif A * B > 0:
        return "Elipse"
    elif A * B < 0:
        return "Hipérbola"
    else:
        return "Parábola"