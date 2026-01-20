def format_string(self, x):
    """
    Convierte una representación de cadena de un número en formato de palabras
    :param x: str, la representación de cadena de un número
    :return: str, el número en formato de palabras
    >>> formatter = NumberWordFormatter()
    >>> formatter.format_string("123456")
    "UNO CIENTO VEINTITRÉS MIL CUATROCIENTOS CINCUENTA Y SEIS SOLAMENTE"
    """
    # Definir las palabras para los números
    unidades = ["", "UNO", "DOS", "TRES", "CUATRO", "CINCO", "SEIS", "SIETE", "OCHO", "NUEVE"]
    decenas_especiales = ["DIEZ", "ONCE", "DOCE", "TRECE", "CATORCE", "QUINCE", "DIECISÉIS", 
                          "DIECISIETE", "DIECIOCHO", "DIECINUEVE"]
    decenas = ["", "", "VEINTE", "TREINTA", "CUARENTA", "CINCUENTA", "SESENTA", "SETENTA", "OCHENTA", "NOVENTA"]
    centenas = ["", "CIENTO", "DOSCIENTOS", "TRESCIENTOS", "CUATROCIENTOS", "QUINIENTOS", 
                "SEISCIENTOS", "SETECIENTOS", "OCHOCIENTOS", "NOVECIENTOS"]
    
    def convertir_centenas(num):
        if num == 0:
            return ""
        elif num == 100:
            return "CIEN"
        elif num < 10:
            return unidades[num]
        elif num < 20:
            return decenas_especiales[num - 10]
        elif num < 100:
            d = num // 10
            u = num % 10
            if d == 2 and u > 0:
                return "VEINTI" + unidades[u]
            elif u == 0:
                return decenas[d]
            else:
                return decenas[d] + " Y " + unidades[u]
        else:
            c = num // 100
            resto = num % 100
            if resto == 0:
                if num == 100:
                    return "CIEN"
                return centenas[c]
            else:
                return centenas[c] + " " + convertir_centenas(resto)
    
    num = int(x)
    
    if num == 0:
        return "CERO SOLAMENTE"
    
    # Dividir en grupos de miles
    millones = num // 1000000
    miles = (num % 1000000) // 1000
    unidades_num = num % 1000
    
    resultado = []
    
    if millones > 0:
        if millones == 1:
            resultado.append("UN MILLÓN")
        else:
            resultado.append(convertir_centenas(millones) + " MILLONES")
    
    if miles > 0:
        if miles == 1:
            resultado.append("UN MIL")
        else:
            resultado.append(convertir_centenas(miles) + " MIL")
    
    if unidades_num > 0:
        resultado.append(convertir_centenas(unidades_num))
    
    return " ".join(resultado) + " SOLAMENTE"