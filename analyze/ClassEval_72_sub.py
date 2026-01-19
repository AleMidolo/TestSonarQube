import re

def sub(self, pattern, replacement, text):
    """
    Reemplaza la subcadena coincidente con una expresión regular por la cadena especificada
    :param pattern: cadena, Patrón de expresión regular
    :param replacement: Texto con el que reemplazar
    :param text: cadena, Texto a ser reemplazado
    :return: cadena, Texto después del reemplazo
    >>> ru = RegexUtils()
    >>> ru.sub(r'\b\d{3}-\d{3}-\d{4}\b', 'phone num',  "123-456-7890 abiguygusu 876-286-9876 kjgufwycs 987-762-9767")
    'phone num abiguygusu phone num kjgufwycs phone num'
    """
    return re.sub(pattern, replacement, text)