def remove_stop_words(self, string_list, stop_word_list):
    """
        Rimuove tutte le le stop word dalla lista di stringhe.
        :param string_list: una lista di stringhe
        :param stop_word_list: una lista di parole di stop
        :return: una lista di parole senza parole di stop
        >>> NLPDataProcessor().remove_stop_words(['This is a test.'], ['a', 'an', 'the'])
        [['This', 'is', 'test.']]
        """
    processed_list = []
    for string in string_list:
        words = string.split()
        filtered_words = [word for word in words if word.lower() not in stop_word_list]
        processed_list.append(filtered_words)
    return processed_list