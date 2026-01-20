def trans_three(self, s):
    """
    Convierte un número de tres dígitos en formato de palabras
    :param s: str, el número de tres dígitos
    :return: str, el número en formato de palabras
    >>> formatter = NumberWordFormatter()
    >>> formatter.trans_three("123")
    "UNO CIENTO Y VEINTE TRES"
    """
    ones = ["", "UNO", "DOS", "TRES", "CUATRO", "CINCO", "SEIS", "SIETE", "OCHO", "NUEVE"]
    tens = ["", "", "VEINTE", "TREINTA", "CUARENTA", "CINCUENTA", "SESENTA", "SETENTA", "OCHENTA", "NOVENTA"]
    teens = ["DIEZ", "ONCE", "DOCE", "TRECE", "CATORCE", "QUINCE", "DIECISEIS", "DIECISIETE", "DIECIOCHO", "DIECINUEVE"]
    hundreds = ["", "CIENTO", "DOSCIENTOS", "TRESCIENTOS", "CUATROCIENTOS", "QUINIENTOS", "SEISCIENTOS", "SETECIENTOS", "OCHOCIENTOS", "NOVECIENTOS"]
    
    s = s.zfill(3)  # Asegurar que tiene 3 dígitos
    result = []
    
    # Centenas
    h = int(s[0])
    if h > 0:
        if h == 1 and s[1:] == "00":
            result.append("CIEN")
        else:
            result.append(hundreds[h])
    
    # Decenas y unidades
    t = int(s[1])
    u = int(s[2])
    
    if t == 0:
        if u > 0:
            result.append(ones[u])
    elif t == 1:
        result.append(teens[u])
    elif t == 2:
        if u == 0:
            result.append("VEINTE")
        else:
            result.append("VEINTI" + ones[u])
    else:
        if u == 0:
            result.append(tens[t])
        else:
            result.append(tens[t] + " Y " + ones[u])
    
    return " Y ".join(result) if len(result) > 1 else (result[0] if result else "")