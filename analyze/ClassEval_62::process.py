def process(self, string_list):
    """
        Construct a stop word list including 'a', 'an', 'the', and remove all the stop words from the list of strings.
        :param string_list: a list of strings
        :return: a list of words without stop words
        >>> NLPDataProcessor.process(['This is a test.'])
        [['This', 'is', 'test.']]
        """
    stop_word_list = self.construct_stop_word_list()
    return self.remove_stop_words(string_list, stop_word_list)