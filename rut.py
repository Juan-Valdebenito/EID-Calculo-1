def validar_rut_detallado(rut):
    cuerpo, dv = rut.split("-")

    print("\n--- VALIDACION RUT ---")

    suma = 0
    multiplo = 2

    for d in reversed(cuerpo):
        print(f"{d} * {multiplo}")
        suma += int(d) * multiplo
        multiplo += 1
        if multiplo > 7:
            multiplo = 2

    print(f"Suma = {suma}")

    resto = suma % 11
    print(f"Resto = {resto}")

    dv_calc = 11 - resto

    if dv_calc == 11:
        dv_calc = "0"
    elif dv_calc == 10:
        dv_calc = "K"
    else:
        dv_calc = str(dv_calc)

    print(f"DV calculado = {dv_calc}")

    return dv_calc == dv.upper()


def obtener_digitos(rut):
    cuerpo, dv = rut.split("-")
    return [int(x) for x in cuerpo], dv


def calcular_v(dv):
    if dv == "K":
        return 10
    elif dv == "0":
        return 11
    return int(dv)