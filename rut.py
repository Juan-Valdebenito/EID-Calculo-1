def limpiar_rut(rut):
    return rut.replace(".", "").replace(" ", "").upper()


def validar_rut_detallado(rut):

    reporte = ""

    rut = limpiar_rut(rut)

    if rut.strip() == "":
        reporte += "Error: Debe ingresar un RUT.\n"
        return False, reporte

    reporte += "\n--- VALIDACIÓN RUT ---\n"

    if "-" not in rut:
        reporte += "Formato inválido: falta el guion.\n"
        return False, reporte

    partes = rut.split("-")

    if len(partes) != 2:
        reporte += "Formato inválido.\n"
        return False, reporte

    cuerpo, dv = partes

    if len(cuerpo) not in [7, 8] or not cuerpo.isdigit():
        reporte += "Formato inválido: el cuerpo del RUT debe tener 7 u 8 dígitos.\n"
        return False, reporte

    cuerpo = cuerpo.zfill(8)

    if len(dv) != 1 or not (dv.isdigit() or dv == "K"):
        reporte += "Formato inválido: el dígito verificador debe ser número o K.\n"
        return False, reporte

    suma = 0
    multiplo = 2
    productos = []

    for digito in reversed(cuerpo):

        producto = int(digito) * multiplo

        productos.append(f"{digito}×{multiplo}")

        suma += producto

        multiplo += 1

        if multiplo > 7:
            multiplo = 2

    reporte += "\nMultiplicación desde derecha a izquierda:\n"
    reporte += " + ".join(productos) + "\n"

    reporte += f"\nSuma = {suma}\n"

    resto = suma % 11

    reporte += f"{suma} mod 11 = {resto}\n"

    resultado = 11 - resto

    reporte += f"11 - {resto} = {resultado}\n"

    if resultado == 11:

        dv_calc = "0"

        reporte += (
            "Como el resultado es 11, "
            "el DV calculado se reemplaza por 0.\n"
        )

    elif resultado == 10:

        dv_calc = "K"

        reporte += (
            "Como el resultado es 10, "
            "el DV calculado se reemplaza por K.\n"
        )

    else:

        dv_calc = str(resultado)

    reporte += f"\nDV calculado = {dv_calc}\n"
    reporte += f"DV ingresado = {dv}\n"

    if dv_calc == dv:

        reporte += "\nConclusión: RUT válido.\n"

        return True, reporte

    else:

        reporte += "\nConclusión: RUT inválido.\n"

        return False, reporte


def obtener_digitos(rut):

    rut = limpiar_rut(rut)

    valido, _ = validar_rut_detallado(rut)

    if not valido:
        return None, None

    partes = rut.split("-")

    if len(partes) != 2:
        return None, None

    cuerpo, dv = partes

    cuerpo = cuerpo.zfill(8)

    return [int(x) for x in cuerpo], dv


def calcular_v(dv):

    if dv == "K":
        return 10

    elif dv == "0":
        return 11

    return int(dv)
