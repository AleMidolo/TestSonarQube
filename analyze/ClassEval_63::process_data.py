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
        cleaned_string = re.sub('[^a-zA-Z\\s]', '', string)
        cleaned_string = cleaned_string.lower()
        words = [word for word in cleaned_string.split() if word]
        words_list.append(words)
    return words_list