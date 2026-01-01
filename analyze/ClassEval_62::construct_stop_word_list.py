def construct_stop_word_list(self):
    """
        Construct a stop word list including 'a', 'an', 'the'.
        :return: a stop word list
        >>> NLPDataProcessor().construct_stop_word_list()
        ['a', 'an', 'the']
        """
    return ['a', 'an', 'the']