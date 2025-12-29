def construct_stop_word_list(self):
    """
        'a', 'an', 'the' सहित एक स्टॉप वर्ड सूची बनाएं।
        :return: स्टॉप वर्ड की एक सूची
        >>> NLPDataProcessor.construct_stop_word_list()
        ['a', 'an', 'the']
        """
    return ['a', 'an', 'the']