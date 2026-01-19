def remove_stop_words(self, string_list, stop_word_list):
    """
    सूची से सभी स्टॉप शब्दों को हटा दें।
    :param string_list: स्ट्रिंग्स की एक सूची
    :param stop_word_list: स्टॉप शब्दों की एक सूची
    :return: बिना स्टॉप शब्दों के शब्दों की एक सूची
    >>> NLPDataProcessor.process(['This is a test.'])
    [['This', 'is', 'test.']]
    """
    result = []
    for string in string_list:
        words = string.split()
        filtered_words = [word for word in words if word not in stop_word_list]
        result.append(filtered_words)
    return result