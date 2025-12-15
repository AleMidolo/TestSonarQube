class NLPDataProcessor: 

    def construct_stop_word_list(self):
        """
        Construct a stop word list including 'a', 'an', 'the'.
        :return: a list of stop words
        >>> NLPDataProcessor.construct_stop_word_list()
        ['a', 'an', 'the']
        """
        stop_word_list = ['a', 'an', 'the']
        return stop_word_list
    
    def remove_stop_words(self, string_list, stop_word_list):
        """
        Remove all the stop words from the list of strings.
        :param string_list: a list of strings
        :param stop_word_list: a list of stop words
        :return: a list of words without stop words
        >>> NLPDataProcessor.remove_stop_words(['This is a test.'], ['a', 'an', 'the'])
        [['This', 'is', 'test.']]
        """
        answer = []
        for string in string_list:
            string_split = string.split()
            for word in string_split[:]:  # Iterate over a copy of the list
                if word in stop_word_list:
                    string_split.remove(word)
            answer.append(string_split)
        return answer
    
    def process(self, string_list):
        """
        Costruisce un elenco di stop word che include 'a', 'an', 'the', e rimuove tutte le stop word dall'elenco di stringhe.
        :param string_list: un elenco di stringhe
        :return: un elenco di parole senza stop word
        >>> NLPDataProcessor.process(['This is a test.'])
        [['This', 'is', 'test.']]
        """
        stop_word_list = self.construct_stop_word_list()
        return self.remove_stop_words(string_list, stop_word_list)