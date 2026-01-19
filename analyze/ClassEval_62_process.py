def process(self, string_list):
    """
    Construye una lista de palabras vacías que incluye 'a', 'an', 'the', y elimina todas las palabras vacías de la lista de cadenas.
    :param string_list: una lista de cadenas
    :return: una lista de palabras sin palabras vacías
    >>> NLPDataProcessor.process(['This is a test.'])
    [['This', 'is', 'test.']]
    """
    stop_words = {'a', 'an', 'the'}
    result = []
    
    for string in string_list:
        words = string.split()
        filtered_words = [word for word in words if word.lower() not in stop_words]
        result.append(filtered_words)
    
    return result