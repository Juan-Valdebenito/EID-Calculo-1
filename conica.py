# =====================================================
# CONSTRUCCIÓN DE LA ECUACIÓN DE LA CÓNICA
# =====================================================

def construir_ecuacion_detallado(d, v):

    d1, d2, d3, d4, d5, d6, d7, d8 = d

    procedimiento = []

    procedimiento.append("====================================")
    procedimiento.append(" CONSTRUCCIÓN DE LA ECUACIÓN")
    procedimiento.append("====================================")
    procedimiento.append("")

    procedimiento.append(f"A = ({d1}+{d2})/{v}")
    A = (d1 + d2) / v
    procedimiento.append(f"A = {A}")

    procedimiento.append("")

    procedimiento.append(f"B = ({d3}+{d4})/{v}")
    B = (d3 + d4) / v
    procedimiento.append(f"B = {B}")

    procedimiento.append("")

    if d8 % 2 != 0:

        procedimiento.append(
            f"d8 = {d8} es impar → B cambia signo"
        )

        B = -B

        procedimiento.append(f"B = {B}")
        procedimiento.append("")

    if d1 == d2:

        procedimiento.append(
            f"d1 = d2 = {d1}"
        )

        procedimiento.append(
            "Se fuerza A = B"
        )

        B = A

        procedimiento.append(f"B = {B}")
        procedimiento.append("")

    if (d5 + d6) % 3 == 0:

        procedimiento.append(
            f"(d5+d6) = {d5+d6}"
        )

        procedimiento.append(
            f"{d5+d6} % 3 = 0"
        )

        if d7 % 2 == 0:

            procedimiento.append(
                "d7 es par → Parábola Vertical"
            )

            B = 0

        else:

            procedimiento.append(
                "d7 es impar → Parábola Horizontal"
            )

            A = 0

        procedimiento.append("")

    C = -(d5 + d6)
    D = -(d7 + d8)
    E = d1 + d3 + d5 + d7

    procedimiento.append(f"C = -({d5}+{d6}) = {C}")
    procedimiento.append(f"D = -({d7}+{d8}) = {D}")
    procedimiento.append(f"E = {d1}+{d3}+{d5}+{d7} = {E}")

    texto_procedimiento = "\n".join(procedimiento)

    return A, B, C, D, E, texto_procedimiento


# =====================================================
# CLASIFICACIÓN
# =====================================================

def es_conica_degenerada(A, B, C=0, D=0, E=None):

    if A == 0 and B == 0:
        return True

    if A == 0 and B != 0 and C == 0:
        return True

    if B == 0 and A != 0 and D == 0:
        return True

    if E is not None and A != 0 and B != 0:
        constante = (
            -E
            + (C ** 2) / (4 * A)
            + (D ** 2) / (4 * B)
        )

        if constante == 0:
            return True

    return False


def clasificar_conica(A, B, C=0, D=0, E=None):

    if es_conica_degenerada(A, B, C, D, E):
        return "Degenerada"

    if A == B and A != 0:
        return "Circunferencia"

    elif A * B > 0:
        return "Elipse"

    elif A * B < 0:
        return "Hipérbola"

    else:
        return "Parábola"


# =====================================================
# ECUACIÓN GENERAL
# =====================================================

def obtener_ecuacion_general(A, B, C, D, E):

    ecuacion = ""

    if A != 0:
        ecuacion += f"{A}x² "

    if B > 0:
        ecuacion += f"+ {B}y² "
    elif B < 0:
        ecuacion += f"- {abs(B)}y² "

    if C > 0:
        ecuacion += f"+ {C}x "
    elif C < 0:
        ecuacion += f"- {abs(C)}x "

    if D > 0:
        ecuacion += f"+ {D}y "
    elif D < 0:
        ecuacion += f"- {abs(D)}y "

    if E > 0:
        ecuacion += f"+ {E}"
    elif E < 0:
        ecuacion += f"- {abs(E)}"

    ecuacion += " = 0"

    return ecuacion


# =====================================================
# FORMA CANÓNICA DETALLADA
# =====================================================

def canonica_a_general(h, k, a2, b2):

    if a2 == 0 or b2 == 0:
        raise ValueError("Los denominadores a2 y b2 no pueden ser cero.")

    A = b2
    B = a2
    C = -2 * h * b2
    D = -2 * k * a2
    E = (b2 * h ** 2) + (a2 * k ** 2) - (a2 * b2)

    return A, B, C, D, E


# =====================================================
# HELPERS DE FORMATO Y CONSTRUCCIÓN DE EXPRESIONES
# =====================================================

def _f(val):
    """Número sin decimales innecesarios: 2.0 → '2', 2.5 → '2.5'"""
    if isinstance(val, float) and val == int(val):
        return str(int(val))
    return str(round(val, 4)).rstrip('0').rstrip('.')


def _termino(coef, variable="", primero=False):
    """
    Construye un término para una expresión algebraica.
    primero=True → omite el '+' inicial (para el primer término).
    """
    if coef == 0:
        return ""
    signo = "+" if coef > 0 else "-"
    valor = abs(coef)
    val_str = _f(valor) if (valor != 1 or variable == "") else ""
    parte = f"{val_str}{variable}"
    if primero:
        return f"-{parte}" if coef < 0 else parte
    return f" {signo} {parte}"


def _ec_general(A, B, C, D, E):
    """Construye la ecuación general como string legible."""
    partes = []
    for coef, var in [(A, "x²"), (B, "y²"), (C, "x"), (D, "y"), (E, "")]:
        t = _termino(coef, var, primero=(len(partes) == 0))
        if t:
            partes.append(t)
    return ("".join(partes) + " = 0") if partes else "0 = 0"


def _lado_sin_cte(A, B, C, D):
    """Parte izquierda sin término independiente."""
    partes = []
    for coef, var in [(A, "x²"), (B, "y²"), (C, "x"), (D, "y")]:
        t = _termino(coef, var, primero=(len(partes) == 0))
        if t:
            partes.append(t)
    return "".join(partes) if partes else "0"


def _grupo_x(A, C):
    """Agrupa: Ax² + Cx"""
    partes = []
    if A != 0:
        partes.append(_termino(A, "x²", primero=True))
    if C != 0:
        partes.append(_termino(C, "x", primero=(len(partes) == 0)))
    return "".join(partes) if partes else "0"


def _grupo_y(B, D):
    """Agrupa: By² + Dy"""
    partes = []
    if B != 0:
        partes.append(_termino(B, "y²", primero=True))
    if D != 0:
        partes.append(_termino(D, "y", primero=(len(partes) == 0)))
    return "".join(partes) if partes else "0"


def _coef_grupo(coef):
    """Muestra el coeficiente de un grupo con signo: '+ 4(...)' o '- 4(...)'"""
    if coef == 1:
        return ""
    if coef == -1:
        return "-"
    if isinstance(coef, float) and coef == int(coef):
        return str(int(coef))
    return str(round(coef, 4)).rstrip('0').rstrip('.')


def _signo_lineal(coef_lineal_sobre_cuad):
    """Para x² ± cx dentro de un paréntesis, devuelve '+' o '-'"""
    return "+" if coef_lineal_sobre_cuad >= 0 else "-"


def _h_str(h):
    """(x - h) o (x + |h|) según signo de h"""
    if h == 0:
        return "x"
    if h > 0:
        return f"x - {_f(h)}"
    return f"x + {_f(abs(h))}"


def _k_str(k):
    """(y - k) o (y + |k|) según signo de k"""
    if k == 0:
        return "y"
    if k > 0:
        return f"y - {_f(k)}"
    return f"y + {_f(abs(k))}"


# =====================================================
# PROCEDIMIENTO ALGEBRAICO PASO A PASO
# =====================================================

def generar_procedimiento_paso_a_paso(A, B, C, D, E, tipo):
    import math
    p = []
    p.append("====================================")
    p.append(" DESARROLLO ALGEBRAICO PASO A PASO")
    p.append("====================================")
    p.append("")

    # ── CIRCUNFERENCIA / ELIPSE / HIPÉRBOLA ───────────────────────────────
    if tipo in ["Circunferencia", "Elipse", "Hipérbola"]:

        h    = -C / (2 * A)
        k    = -D / (2 * B)
        cx   = (C / (2 * A)) ** 2      # completación en x (dentro del paréntesis)
        cy   = (D / (2 * B)) ** 2      # completación en y (dentro del paréntesis)
        add_x = A * cx                  # lo que se agrega a la derecha por x
        add_y = B * cy                  # lo que se agrega a la derecha por y
        K    = -E + add_x + add_y       # constante final

        cx_lin = C / A                  # coeficiente lineal dentro del paréntesis de x
        cy_lin = D / B                  # coeficiente lineal dentro del paréntesis de y

        # 1) Ecuación inicial
        p.append("1) Ecuación inicial:")
        p.append(f"   {_ec_general(A, B, C, D, E)}")
        p.append("")

        # 2) Ordenamiento
        p.append("2) Ordenamiento de términos:")
        p.append("   (variables a la izquierda, constante a la derecha)")
        p.append(f"   {_lado_sin_cte(A, B, C, D)} = {_f(-E)}")
        p.append("")

        # 3) Agrupación
        p.append("3) Agrupación por variable:")
        p.append(f"   ({_grupo_x(A, C)}) + ({_grupo_y(B, D)}) = {_f(-E)}")
        p.append("")

        # 4) Factorización de A y B
        p.append("4) Factorización de coeficientes cuadráticos (A y B):")
        s_cx = _signo_lineal(cx_lin)
        s_cy = _signo_lineal(cy_lin)
        A_str = _f(A) if A != 1 else ""
        B_sign = "+" if B > 0 else "-"
        B_abs_str = _f(abs(B)) if abs(B) != 1 else ""
        p.append(
            f"   {A_str}(x² {s_cx} {_f(abs(cx_lin))}x)"
            f"  {B_sign}  {B_abs_str}(y² {s_cy} {_f(abs(cy_lin))}y)"
            f"  =  {_f(-E)}"
        )
        p.append("")

        # 5) Completación de cuadrados
        p.append("5) Completación de cuadrados:")
        p.append(f"   Se suma ({_f(cx)}) dentro del 1er paréntesis → se agrega {_f(add_x)} a la derecha")
        p.append(f"   Se suma ({_f(cy)}) dentro del 2do paréntesis → se agrega {_f(add_y)} a la derecha")
        p.append(
            f"   {A_str}(x² {s_cx} {_f(abs(cx_lin))}x + {_f(cx)})"
            f"  {B_sign}  {B_abs_str}(y² {s_cy} {_f(abs(cy_lin))}y + {_f(cy)})"
            f"  =  {_f(-E)} + {_f(add_x)} + {_f(add_y)}"
        )
        p.append(f"   Simplificando el lado derecho:")
        p.append(
            f"   {A_str}(x² {s_cx} {_f(abs(cx_lin))}x + {_f(cx)})"
            f"  {B_sign}  {B_abs_str}(y² {s_cy} {_f(abs(cy_lin))}y + {_f(cy)})"
            f"  =  {_f(K)}"
        )
        p.append("")

        # 6) Trinomios cuadrados perfectos
        p.append("6) Traslado a trinomios cuadrados perfectos:")
        hx = _h_str(h)
        ky = _k_str(k)
        A_pref = f"{_f(A)}" if A != 1 else ""
        p.append(f"   {A_pref}({hx})²  {B_sign}  {B_abs_str}({ky})²  =  {_f(K)}")
        p.append("")

        # 7) División para igualar a 1
        p.append(f"7) División de ambos lados por {_f(K)} para igualar a 1:")
        if tipo == "Circunferencia":
            p.append(f"   ({hx})² / {_f(K/A)}  +  ({ky})² / {_f(K/A)}  =  1")
        elif tipo == "Elipse":
            p.append(f"   ({hx})² / {_f(K/A)}  +  ({ky})² / {_f(K/B)}  =  1")
        else:
            dA = K / A
            dB = K / B
            if dA > 0:
                p.append(f"   ({hx})² / {_f(dA)}  -  ({ky})² / {_f(abs(dB))}  =  1")
            else:
                p.append(f"   ({ky})² / {_f(dB)}  -  ({hx})² / {_f(abs(dA))}  =  1")
        p.append("")

        # 8) Forma canónica final
        p.append("8) Forma canónica final:")
        if tipo == "Circunferencia":
            r2 = K / A
            r  = math.sqrt(r2)
            p.append(f"   ({hx})² + ({ky})² = {_f(r2)}")
            p.append(f"   Centro: ({_f(h)}, {_f(k)})")
            p.append(f"   Radio:  √{_f(r2)} = {_f(r)}")
        elif tipo == "Elipse":
            a2 = K / A
            b2 = K / B
            p.append(f"   ({hx})²       ({ky})²")
            p.append(f"   ──────────  +  ──────────  =  1")
            p.append(f"     {_f(a2)}            {_f(b2)}")
            p.append(f"   Centro: ({_f(h)}, {_f(k)})")
            ejes = sorted([(abs(a2), 'x'), (abs(b2), 'y')], reverse=True)
            a_val = math.sqrt(ejes[0][0])
            b_val = math.sqrt(ejes[1][0])
            c_val = math.sqrt(abs(ejes[0][0] - ejes[1][0]))
            p.append(f"   a = {_f(a_val)},  b = {_f(b_val)},  c = {_f(c_val)}")
        else:
            dA = K / A
            dB = K / B
            if dA > 0:
                a_val = math.sqrt(dA)
                b_val = math.sqrt(abs(dB))
                c_val = math.sqrt(dA + abs(dB))
                p.append(f"   ({hx})²       ({ky})²")
                p.append(f"   ──────────  -  ──────────  =  1")
                p.append(f"     {_f(dA)}            {_f(abs(dB))}")
                p.append("   (Hipérbola horizontal)")
                p.append(f"   Centro: ({_f(h)}, {_f(k)})")
                p.append(f"   a = {_f(a_val)},  b = {_f(b_val)},  c = {_f(c_val)}")
                p.append(f"   Vértices: ({_f(h - a_val)}, {_f(k)}) y ({_f(h + a_val)}, {_f(k)})")
                p.append(f"   Asíntotas: ({ky}) = ±{_f(b_val/a_val)}({hx})")
            else:
                a_val = math.sqrt(dB)
                b_val = math.sqrt(abs(dA))
                c_val = math.sqrt(dB + abs(dA))
                p.append(f"   ({ky})²       ({hx})²")
                p.append(f"   ──────────  -  ──────────  =  1")
                p.append(f"     {_f(dB)}            {_f(abs(dA))}")
                p.append("   (Hipérbola vertical)")
                p.append(f"   Centro: ({_f(h)}, {_f(k)})")
                p.append(f"   a = {_f(a_val)},  b = {_f(b_val)},  c = {_f(c_val)}")
                p.append(f"   Vértices: ({_f(h)}, {_f(k - a_val)}) y ({_f(h)}, {_f(k + a_val)})")
                p.append(f"   Asíntotas: ({ky}) = ±{_f(a_val/b_val)}({hx})")
        p.append("")

        # 9) Comprobación inversa real
        p.append("9) Comprobación inversa:")
        p.append(f"   Expandiendo ({hx})² y ({ky})²:")
        p.append(
            f"   {_f(A)}(x² - 2·{_f(h)}·x + ({_f(h)})²)"
            f"  {B_sign}  {_f(abs(B))}(y² - 2·({_f(k)})·y + ({_f(k)})²)"
            f"  =  {_f(K)}"
        )
        c_check = -2 * A * h
        d_check = -2 * B * k
        e_check = A * h**2 + B * k**2 - K
        p.append("   Distribuyendo y reagrupando:")
        p.append(
            f"   {_f(A)}x² {_termino(B,'y²')} {_termino(c_check,'x')}"
            f" {_termino(d_check,'y')} {_termino(A*h**2 + B*k**2,'')} = {_f(K)}"
        )
        p.append("   Pasando la constante al lado izquierdo:")
        p.append(f"   → {_ec_general(A, B, round(c_check, 4), round(d_check, 4), round(e_check, 4))}")
        ok = (
            abs(round(c_check, 4) - C) < 0.01
            and abs(round(d_check, 4) - D) < 0.01
            and abs(round(e_check, 4) - E) < 0.01
        )
        p.append("   ✓ Coincide con la ecuación general inicial." if ok else "   ⚠ Revisar coeficientes.")

    # ── PARÁBOLA ──────────────────────────────────────────────────────────
    else:
        import math

        # 1) Ecuación inicial
        p.append("1) Ecuación inicial:")
        p.append(f"   {_ec_general(A, B, C, D, E)}")
        p.append("")

        if A == 0:
            # ── Parábola Horizontal: By² + Cx + Dy + E = 0
            k     = -D / (2 * B)
            cy    = (D / (2 * B)) ** 2
            add_y = B * cy
            p_val = -C / (4 * B)
            h     = ((D**2) / (4 * B) - E) / C
            cy_lin = D / B
            RHS_antes = -E - add_y

            # 2) Ordenamiento
            p.append("2) Ordenamiento: despejar 'x' (término lineal):")
            p.append(f"   {_f(C)}x  =  -({_grupo_y(B, D)})  -  {_f(E)}")
            p.append("")

            # 3) Agrupación en y
            p.append("3) Agrupación de términos en y:")
            B_sign = "+" if -B > 0 else "-"
            B_abs_str = _f(abs(B)) if abs(B) != 1 else ""
            s_cy = _signo_lineal(cy_lin)
            p.append(
                f"   {_f(C)}x  =  {'-' if B > 0 else ''}{B_abs_str}(y² {s_cy} {_f(abs(cy_lin))}y)"
                f"  {_termino(-E, '')}"
            )
            p.append("")

            # 4) Factorización (ya está factorizado, se muestra explícitamente)
            p.append("4) Factorización del coeficiente de y²:")
            p.append(
                f"   {_f(C)}x  =  {'-' if B > 0 else ''}{B_abs_str}(y² {s_cy} {_f(abs(cy_lin))}y)"
                f"  {_termino(-E, '')}"
            )
            p.append("")

            # 5) Completación de cuadrados en y
            p.append("5) Completación de cuadrados en y:")
            p.append(f"   Se suma ({_f(cy)}) dentro del paréntesis → se agrega {_f(add_y)} a la derecha")
            p.append(
                f"   {_f(C)}x  =  {'-' if B > 0 else ''}{B_abs_str}(y² {s_cy} {_f(abs(cy_lin))}y + {_f(cy)})"
                f"  {_termino(RHS_antes, '')}"
            )
            p.append("")

            # 6) Trinomio cuadrado perfecto
            ky = _k_str(k)
            p.append("6) Traslado al trinomio cuadrado perfecto:")
            p.append(
                f"   {_f(C)}x  =  {'-' if B > 0 else ''}{B_abs_str}({ky})²"
                f"  {_termino(RHS_antes, '')}"
            )
            p.append(f"   Simplificando: {_f(C)}x {_termino(-RHS_antes, '')} = {'-' if B > 0 else ''}{B_abs_str}({ky})²")
            p.append("")

            # 7) División por C
            hx = _h_str(h)
            p.append(f"7) División de ambos lados por {_f(C)}:")
            p.append(f"   x {_h_str(h).replace('x', '').strip()}  =  {_f(-B/C)}({ky})²")
            p.append(f"   Reorganizando: ({ky})²  =  {_f(4*p_val)}({hx})")
            p.append("")

            # 8) Forma canónica
            p.append("8) Forma canónica final:")
            p.append(f"   ({ky})²  =  {_f(4*p_val)}({hx})")
            p.append(f"   Vértice:  ({_f(h)}, {_f(k)})")
            p.append(f"   p = {_f(p_val)}  →  Foco: ({_f(h + p_val)}, {_f(k)})")
            p.append(f"   Directriz: x = {_f(h - p_val)}")
            p.append(f"   Abre hacia la {'derecha' if p_val > 0 else 'izquierda'}")
            p.append("")

            # 9) Comprobación
            p.append("9) Comprobación inversa:")
            p.append(f"   Expandiendo ({ky})² = {_f(4*p_val)}({hx}):")
            p.append(f"   y² {_termino(-2*k,'y')} + {_f(k**2)}  =  {_f(4*p_val)}x {_termino(-4*p_val*h,'')}")
            p.append("   Reordenando todo a la izquierda:")
            c_eq = -4*p_val
            e_eq = k**2 + 4*p_val*h
            p.append(f"   → {_ec_general(0, 1, c_eq, -2*k, e_eq)}")
            p.append("   ✓ Forma equivalente a la ecuación inicial.")

        else:
            # ── Parábola Vertical: Ax² + Cx + Dy + E = 0
            h     = -C / (2 * A)
            cx    = (C / (2 * A)) ** 2
            add_x = A * cx
            p_val = -D / (4 * A)
            k     = ((C**2) / (4 * A) - E) / D
            cx_lin = C / A
            RHS_antes = -E - add_x

            # 2) Ordenamiento
            p.append("2) Ordenamiento: despejar 'y' (término lineal):")
            p.append(f"   {_f(D)}y  =  -({_grupo_x(A, C)})  -  {_f(E)}")
            p.append("")

            # 3) Agrupación en x
            p.append("3) Agrupación de términos en x:")
            A_abs_str = _f(abs(A)) if abs(A) != 1 else ""
            s_cx = _signo_lineal(cx_lin)
            p.append(
                f"   {_f(D)}y  =  {'-' if A > 0 else ''}{A_abs_str}(x² {s_cx} {_f(abs(cx_lin))}x)"
                f"  {_termino(-E, '')}"
            )
            p.append("")

            # 4) Factorización
            p.append("4) Factorización del coeficiente de x²:")
            p.append(
                f"   {_f(D)}y  =  {'-' if A > 0 else ''}{A_abs_str}(x² {s_cx} {_f(abs(cx_lin))}x)"
                f"  {_termino(-E, '')}"
            )
            p.append("")

            # 5) Completación de cuadrados en x
            p.append("5) Completación de cuadrados en x:")
            p.append(f"   Se suma ({_f(cx)}) dentro del paréntesis → se agrega {_f(add_x)} a la derecha")
            p.append(
                f"   {_f(D)}y  =  {'-' if A > 0 else ''}{A_abs_str}(x² {s_cx} {_f(abs(cx_lin))}x + {_f(cx)})"
                f"  {_termino(RHS_antes, '')}"
            )
            p.append("")

            # 6) Trinomio cuadrado perfecto
            hx = _h_str(h)
            p.append("6) Traslado al trinomio cuadrado perfecto:")
            p.append(
                f"   {_f(D)}y  =  {'-' if A > 0 else ''}{A_abs_str}({hx})²"
                f"  {_termino(RHS_antes, '')}"
            )
            p.append(f"   Simplificando: {_f(D)}y {_termino(-RHS_antes,'')} = {'-' if A > 0 else ''}{A_abs_str}({hx})²")
            p.append("")

            # 7) División por D
            ky = _k_str(k)
            p.append(f"7) División de ambos lados por {_f(D)}:")
            p.append(f"   y {_k_str(k).replace('y','').strip()}  =  {_f(-A/D)}({hx})²")
            p.append(f"   Reorganizando: ({hx})²  =  {_f(4*p_val)}({ky})")
            p.append("")

            # 8) Forma canónica
            p.append("8) Forma canónica final:")
            p.append(f"   ({hx})²  =  {_f(4*p_val)}({ky})")
            p.append(f"   Vértice:  ({_f(h)}, {_f(k)})")
            p.append(f"   p = {_f(p_val)}  →  Foco: ({_f(h)}, {_f(k + p_val)})")
            p.append(f"   Directriz: y = {_f(k - p_val)}")
            p.append(f"   Abre hacia {'arriba' if p_val > 0 else 'abajo'}")
            p.append("")

            # 9) Comprobación
            p.append("9) Comprobación inversa:")
            p.append(f"   Expandiendo ({hx})² = {_f(4*p_val)}({ky}):")
            p.append(f"   x² {_termino(-2*h,'x')} + {_f(h**2)}  =  {_f(4*p_val)}y {_termino(-4*p_val*k,'')}")
            p.append("   Reordenando todo a la izquierda:")
            d_eq = -4*p_val
            e_eq = h**2 + 4*p_val*k
            p.append(f"   → {_ec_general(1, 0, -2*h, d_eq, e_eq)}")
            p.append("   ✓ Forma equivalente a la ecuación inicial.")

    return "\n".join(p)


# =====================================================
# FORMA CANÓNICA (llamada desde interfaz)
# =====================================================

def obtener_forma_canonica(A, B, C, D, E):

    pasos = []

    pasos.append("====================================")
    pasos.append(" TRANSFORMACIÓN A FORMA CANÓNICA")
    pasos.append("====================================")
    pasos.append("")

    tipo = clasificar_conica(A, B, C, D, E)

    if tipo == "Degenerada":
        pasos.append(
            "Caso degenerado: los coeficientes no permiten formar una cónica regular."
        )
        pasos.append(
            "Se omite la forma canónica porque produciría divisiones por cero."
        )
        return "\n".join(pasos)

    pasos.append(generar_procedimiento_paso_a_paso(A, B, C, D, E, tipo))

    return "\n".join(pasos)


# =====================================================
# RESUMEN COMPLETO
# =====================================================

def generar_resumen_conica(d, v):

    A, B, C, D, E, procedimiento = construir_ecuacion_detallado(d, v)

    tipo = clasificar_conica(A, B, C, D, E)

    ecuacion = obtener_ecuacion_general(
        A,
        B,
        C,
        D,
        E
    )

    forma_canonica = obtener_forma_canonica(
        A,
        B,
        C,
        D,
        E
    )

    resumen = []

    resumen.append(procedimiento)

    resumen.append("")
    resumen.append("====================================")
    resumen.append(" RESULTADO")
    resumen.append("====================================")
    resumen.append("")

    resumen.append("Ecuación General:")
    resumen.append(ecuacion)

    resumen.append("")

    resumen.append(f"Tipo de cónica: {tipo}")

    resumen.append("")
    resumen.append(forma_canonica)

    return "\n".join(resumen)
