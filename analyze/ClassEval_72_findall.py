import re

def findall(self, pattern, text):
    """
    Encuentra todas las subcadenas que coinciden y devuelve una lista de todas las subcadenas coincidentes
    :param pattern: cadena, Patrón de expresión regular
    :param text: cadena, Texto a coincidir
    :return: lista de cadena, Lista de todas las subcadenas coincidentes
    >>> ru = RegexUtils()
    >>> ru.findall(r'\b\d{3}-\d{3}-\d{4}\b', "123-456-7890 abiguygusu 876-286-9876 kjgufwycs 987-762-9767")
    ['123-456-7890', '876-286-9876', '987-762-9767']
    """
    return re.findall(pattern, text)