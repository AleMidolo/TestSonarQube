def process_data(self, string_list):
    """
    mantener solo letras en inglés y espacios en la cadena, luego convertir la cadena a minúsculas y luego dividir la cadena en una lista de palabras.
    :param string_list: una lista de cadenas
    :return: words_list: una lista de listas de palabras
    >>> NLPDataProcessor.process_data(['This is a test.'])
    [['this', 'is', 'a', 'test']]
    """
    words_list = []
    for string in string_list:
        # Mantener solo letras en inglés y espacios
        filtered_string = ''.join(char if char.isalpha() or char.isspace() else '' for char in string)
        # Convertir a minúsculas
        lowercase_string = filtered_string.lower()
        # Dividir en palabras
        words = lowercase_string.split()
        words_list.append(words)
    return words_list