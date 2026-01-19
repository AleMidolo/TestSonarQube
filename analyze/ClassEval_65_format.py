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
    decenas_especiales = ["DIEZ", "ONCE", "DOCE", "TRECE", "CATORCE", "QUINCE", "DIECISÉIS", 
                          "DIECISIETE", "DIECIOCHO", "DIECINUEVE"]
    decenas = ["", "", "VEINTE", "TREINTA", "CUARENTA", "CINCUENTA", "SESENTA", "SETENTA", "OCHENTA", "NOVENTA"]
    centenas = ["", "CIENTO", "DOSCIENTOS", "TRESCIENTOS", "CUATROCIENTOS", "QUINIENTOS", 
                "SEISCIENTOS", "SETECIENTOS", "OCHOCIENTOS", "NOVECIENTOS"]
    
    def convert_group(n):
        """Convierte un grupo de hasta 3 dígitos"""
        if n == 0:
            return ""
        elif n == 100:
            return "CIEN"
        
        result = []
        
        # Centenas
        c = n // 100
        if c > 0:
            result.append(centenas[c])
        
        # Decenas y unidades
        resto = n % 100
        if resto >= 10 and resto < 20:
            result.append(decenas_especiales[resto - 10])
        else:
            d = resto // 10
            u = resto % 10
            
            if d == 2 and u > 0:
                result.append("VEINTI" + unidades[u])
            else:
                if d > 0:
                    result.append(decenas[d])
                if u > 0:
                    if d > 2:
                        result.append("Y")
                    result.append(unidades[u])
        
        return " ".join(result)
    
    # Convertir número entero
    if integer_part == 0:
        words = "CERO"
    else:
        groups = []
        
        # Millones
        millones = integer_part // 1000000
        if millones > 0:
            if millones == 1:
                groups.append("UN MILLÓN")
            else:
                groups.append(convert_group(millones) + " MILLONES")
        
        # Miles
        miles = (integer_part % 1000000) // 1000
        if miles > 0:
            if miles == 1:
                groups.append("MIL")
            else:
                groups.append(convert_group(miles) + " MIL")
        
        # Unidades
        unidades_num = integer_part % 1000
        if unidades_num > 0:
            groups.append(convert_group(unidades_num))
        
        words = " ".join(groups)
    
    # Agregar parte decimal si existe
    if decimal_part:
        words += " CON " + decimal_part + "/100"
    
    return words + " SOLAMENTE"