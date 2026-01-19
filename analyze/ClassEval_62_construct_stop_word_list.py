def construct_stop_word_list(self):
    """
        Construir una lista de palabras vacías que incluya 'a', 'an', 'the'.
        :return: una lista de palabras vacías
        >>> NLPDataProcessor.construct_stop_word_list()
        ['a', 'an', 'the']
        """
    return ['a', 'an', 'the']