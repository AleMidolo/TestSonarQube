def construct_stop_word_list(self):
    """
        Costruisce un elenco di parole vuote includendo 'a', 'an', 'the'.
        :return: un elenco di parole vuote
        >>> NLPDataProcessor().construct_stop_word_list()
        ['a', 'an', 'the']
        """
    return ['a', 'an', 'the']