def limpiar_rut(rut):
    return rut.replace(".", "").replace(" ", "").upper()

def validar_rut_detallado(rut):
    rut = limpiar_rut(rut)
    cuerpo, dv = rut.split("-")

    print("\n--- VALIDACION RUT ---")

    if "-" not in rut:
        print("Formato inválido: falta el guion.")
        return False

    cuerpo, dv = rut.split("-")

    if len(cuerpo) not in [7, 8] or not cuerpo.isdigit():
        print("Formato inválido: el cuerpo del RUT debe tener 7 u 8 dígitos.")
        return False

    cuerpo = cuerpo.zfill(8)  

    if len(dv) != 1 or not (dv.isdigit() or dv == "K"):
        print("Formato inválido: el dígito verificador debe ser número o K.")
        return False

    suma = 0
    multiplo = 2
    productos = []

    for digito in reversed(cuerpo):
        producto = int(digito) * multiplo
        productos.append(f"{digito}·{multiplo}")
        suma += producto

        multiplo += 1
        if multiplo > 7:
            multiplo = 2

    print("\nMultiplicación desde derecha a izquierda:")
    print(" + ".join(productos))

    print(f"\nSuma = {suma}")

    resto = suma % 11
    print(f"{suma} mod 11 = {resto}")

    resultado = 11 - resto
    print(f"11 - {resto} = {resultado}")    

    if resultado == 11:
        dv_calc = "0"
        print("Como el resultado es 11, el DV calculado se reemplaza por 0.")
    elif resultado == 10:
        dv_calc = "K"
        print("Como el resultado es 10, el DV calculado se reemplaza por K.")
    else:
        dv_calc = str(resultado)
#        print(f"DV calculado: {dv_calc}")

    print(f"\nDV calculado = {dv_calc}")
    print(f"DV ingresado = {dv}")

    if dv_calc == dv:
        print("\nConclusión: RUT válido.")
        return True
    else:
        print("\nConclusión: RUT inválido.")
        return False


def obtener_digitos(rut):
    rut = limpiar_rut(rut)
    cuerpo, dv = rut.split("-")
    cuerpo = cuerpo.zfill(8)
    return [int(x) for x in cuerpo], dv


def calcular_v(dv):
    if dv == "K":
        return 10
    elif dv == "0":
        return 11
    return int(dv)

#validar_rut_detallado("2079.33.11-2") # valido
#validar_rut_detallado("2079.33.11-3") # invalido