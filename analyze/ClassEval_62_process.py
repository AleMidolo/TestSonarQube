def process(self, string_list):
    """
        Construye una lista de palabras vacías que incluye 'a', 'an', 'the', y elimina todas las palabras vacías de la lista de cadenas.
        :param string_list: una lista de cadenas
        :return: una lista de palabras sin palabras vacías
        >>> NLPDataProcessor.process(['This is a test.'])
        [['This', 'is', 'test.']]
        """
    stop_word_list = self.construct_stop_word_list()
    return self.remove_stop_words(string_list, stop_word_list)