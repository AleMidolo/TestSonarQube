def remove_stop_words(self, string_list, stop_word_list):
    """
        Elimina todas las palabras vacías de la lista de cadenas.
        :param string_list: una lista de cadenas
        :param stop_word_list: una lista de palabras vacías
        :return: una lista de palabras sin palabras vacías
        >>> NLPDataProcessor.process(['This is a test.'])
        [['This', 'is', 'test.']]
        """
    processed_list = []
    for string in string_list:
        words = string.split()
        filtered_words = [word for word in words if word.lower() not in stop_word_list]
        processed_list.append(filtered_words)
    return processed_list