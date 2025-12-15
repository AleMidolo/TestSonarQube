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
        >>> NLPDataProcessor.process(['This is a test.'])
        [['This', 'is', 'test.']]
        """
        answer = []
        for string in string_list:
            string_split = string.split()
            for word in string_split:
                if word in stop_word_list:
                    string_split.remove(word)
            answer.append(string_split)
        return answer
    
    @classmethod
    def process(cls, string_list):
        """
        'a', 'an', 'the' सहित एक स्टॉप वर्ड सूची बनाएं, और स्ट्रिंग्स की सूची से सभी स्टॉप वर्ड हटा दें।
        :param string_list: स्ट्रिंग्स की एक सूची
        :return: बिना स्टॉप वर्ड के शब्दों की एक सूची
        >>> NLPDataProcessor.process(['This is a test.'])
        [['This', 'is', 'test.']]
        """
        stop_word_list = cls.construct_stop_word_list(cls)
        return cls.remove_stop_words(cls, string_list, stop_word_list)