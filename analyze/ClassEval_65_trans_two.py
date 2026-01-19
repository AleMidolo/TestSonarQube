def trans_two(self, s):
    """
    Convierte un número de dos dígitos en formato de palabras
    :param s: str, el número de dos dígitos
    :return: str, el número en formato de palabras
    >>> formatter = NumberWordFormatter()
    >>> formatter.trans_two("23")
    "VEINTITRÉS"
    """
    num = int(s)
    
    # Casos especiales del 10 al 15
    especiales = {
        10: "DIEZ",
        11: "ONCE",
        12: "DOCE",
        13: "TRECE",
        14: "CATORCE",
        15: "QUINCE"
    }
    
    if num in especiales:
        return especiales[num]
    
    # Del 16 al 19
    unidades = ["", "UNO", "DOS", "TRES", "CUATRO", "CINCO", "SEIS", "SIETE", "OCHO", "NUEVE"]
    if 16 <= num <= 19:
        return "DIECISÉIS" if num == 16 else f"DIECI{unidades[num % 10]}"
    
    # Del 20 al 29
    if 20 <= num <= 29:
        if num == 20:
            return "VEINTE"
        veinte_map = {
            21: "VEINTIUNO",
            22: "VEINTIDÓS",
            23: "VEINTITRÉS",
            24: "VEINTICUATRO",
            25: "VEINTICINCO",
            26: "VEINTISÉIS",
            27: "VEINTISIETE",
            28: "VEINTIOCHO",
            29: "VEINTINUEVE"
        }
        return veinte_map[num]
    
    # Del 30 en adelante
    decenas = ["", "", "VEINTE", "TREINTA", "CUARENTA", "CINCUENTA", 
               "SESENTA", "SETENTA", "OCHENTA", "NOVENTA"]
    
    decena = num // 10
    unidad = num % 10
    
    if unidad == 0:
        return decenas[decena]
    else:
        return f"{decenas[decena]} Y {unidades[unidad]}"