def format(self, x):
    """
    Convierte un número en formato de palabras
    :param x: int o float, el número que se va a convertir en formato de palabras
    :return: str, el número en formato de palabras
    >>> formatter = NumberWordFormatter()
    >>> formatter.format(123456)
    "CIENTO VEINTITRÉS MIL CUATROCIENTOS CINCUENTA Y SEIS SOLAMENTE"
    """
    if x == 0:
        return "CERO SOLAMENTE"
    
    # Separar parte entera y decimal
    if isinstance(x, float):
        parts = str(x).split('.')
        integer_part = int(parts[0])
        decimal_part = parts[1] if len(parts) > 1 else None
    else:
        integer_part = int(x)
        decimal_part = None
    
    # Definir palabras básicas
    unidades = ["", "UNO", "DOS", "TRES", "CUATRO", "CINCO", "SEIS", "SIETE", "OCHO", "NUEVE"]
    diez_a_quince = ["DIEZ", "ONCE", "DOCE", "TRECE", "CATORCE", "QUINCE"]
    veintis = ["", "", "VEINTI", "VEINTI", "VEINTI", "VEINTI", "VEINTI", "VEINTI", "VEINTI", "VEINTI"]
    decenas = ["", "", "VEINTE", "TREINTA", "CUARENTA", "CINCUENTA", "SESENTA", "SETENTA", "OCHENTA", "NOVENTA"]
    centenas = ["", "CIENTO", "DOSCIENTOS", "TRESCIENTOS", "CUATROCIENTOS", "QUINIENTOS", "SEISCIENTOS", "SETECIENTOS", "OCHOCIENTOS", "NOVECIENTOS"]
    
    def convert_group(n):
        if n == 0:
            return ""
        elif n == 100:
            return "CIEN"
        elif n < 10:
            return unidades[n]
        elif n < 16:
            return diez_a_quince[n - 10]
        elif n < 20:
            return "DIECI" + unidades[n - 10]
        elif n < 30:
            if n == 20:
                return "VEINTE"
            else:
                return veintis[2] + unidades[n - 20]
        elif n < 100:
            dec = n // 10
            uni = n % 10
            if uni == 0:
                return decenas[dec]
            else:
                return decenas[dec] + " Y " + unidades[uni]
        else:
            cen = n // 100
            resto = n % 100
            if resto == 0:
                return centenas[cen]
            else:
                return centenas[cen] + " " + convert_group(resto)
    
    result = ""
    
    if integer_part >= 1000000:
        millones = integer_part // 1000000
        if millones == 1:
            result += "UN MILLÓN"
        else:
            result += convert_group(millones) + " MILLONES"
        integer_part %= 1000000
        if integer_part > 0:
            result += " "
    
    if integer_part >= 1000:
        miles = integer_part // 1000
        if miles == 1:
            result += "MIL"
        else:
            result += convert_group(miles) + " MIL"
        integer_part %= 1000
        if integer_part > 0:
            result += " "
    
    if integer_part > 0:
        result += convert_group(integer_part)
    
    result = result.strip() + " SOLAMENTE"
    
    return result