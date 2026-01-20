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
        return "DIECISÉIS" if num == 16 else "DIECI" + unidades[num % 10]
    
    # Del 20 al 29
    if 20 <= num <= 29:
        if num == 20:
            return "VEINTE"
        unidad = num % 10
        if unidad == 0:
            return "VEINTE"
        veintis = {
            1: "VEINTIUNO", 2: "VEINTIDÓS", 3: "VEINTITRÉS", 4: "VEINTICUATRO",
            5: "VEINTICINCO", 6: "VEINTISÉIS", 7: "VEINTISIETE", 8: "VEINTIOCHO", 9: "VEINTINUEVE"
        }
        return veintis[unidad]
    
    # Del 30 al 99
    decenas = {
        3: "TREINTA", 4: "CUARENTA", 5: "CINCUENTA",
        6: "SESENTA", 7: "SETENTA", 8: "OCHENTA", 9: "NOVENTA"
    }
    
    decena = num // 10
    unidad = num % 10
    
    if unidad == 0:
        return decenas[decena]
    else:
        return decenas[decena] + " Y " + unidades[unidad]