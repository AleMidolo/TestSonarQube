def construct_stop_word_list(self):
    """
        Construct a list of stop words that includes 'a', 'an', 'the'.
        :return: a list of stop words
        >>> NLPDataProcessor().construct_stop_word_list()
        ['a', 'an', 'the']
        """
    return ['a', 'an', 'the']