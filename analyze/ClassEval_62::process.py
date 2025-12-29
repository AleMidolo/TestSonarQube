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