def remove_stop_words(self, string_list, stop_word_list):
    """
        Remove all the stop words from the list of strings.
        :param string_list: a list of strings
        :param stop_word_list: a list of stop words
        :return: a list of words without stop words
        >>> NLPDataProcessor().remove_stop_words(['This is a test.'], ['a', 'an', 'the'])
        [['This', 'is', 'test.']]
        """
    processed_list = []
    for string in string_list:
        words = string.split()
        filtered_words = [word for word in words if word.lower() not in stop_word_list]
        processed_list.append(filtered_words)
    return processed_list