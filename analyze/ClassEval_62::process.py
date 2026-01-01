@classmethod
def process(cls, string_list):
    """
        Costruisce un elenco di stop word che include 'a', 'an', 'the', e rimuove tutte le stop word dall'elenco di stringhe.
        :param string_list: un elenco di stringhe
        :return: un elenco di parole senza stop word
        >>> NLPDataProcessor.process(['This is a test.'])
        [['This', 'is', 'test.']]
        """
    stop_word_list = cls.construct_stop_word_list(cls)
    return cls.remove_stop_words(cls, string_list, stop_word_list)