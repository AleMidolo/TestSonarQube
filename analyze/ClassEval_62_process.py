def process(self, string_list):
    """
    Costruisce un elenco di stop word che include 'a', 'an', 'the', e rimuove tutte le stop word dall'elenco di stringhe.
    :param string_list: un elenco di stringhe
    :return: un elenco di parole senza stop word
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