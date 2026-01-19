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
    teens = ["DIEZ", "ONCE", "DOCE", "TRECE", "CATORCE", "QUINCE", "DIECISEIS", "DIECISIETE", "DIECIOCHO", "DIECINUEVE"]
    tens = ["", "", "VEINTE", "TREINTA", "CUARENTA", "CINCUENTA", "SESENTA", "SETENTA", "OCHENTA", "NOVENTA"]
    hundreds = ["", "CIENTO", "DOSCIENTOS", "TRESCIENTOS", "CUATROCIENTOS", "QUINIENTOS", "SEISCIENTOS", "SETECIENTOS", "OCHOCIENTOS", "NOVECIENTOS"]
    
    s = s.zfill(3)  # Asegurar que tiene 3 dígitos
    h = int(s[0])  # centenas
    t = int(s[1])  # decenas
    o = int(s[2])  # unidades
    
    result = []
    
    # Centenas
    if h > 0:
        if h == 1 and t == 0 and o == 0:
            result.append("CIEN")
        else:
            result.append(hundreds[h])
    
    # Decenas y unidades
    if t == 1:  # 10-19
        result.append(teens[o])
    elif t == 2 and o > 0:  # 21-29
        result.append("VEINTI" + ones[o])
    else:
        if t > 0:
            result.append(tens[t])
        if o > 0:
            if t > 2:
                result.append("Y")
            result.append(ones[o])
    
    return " ".join(result)