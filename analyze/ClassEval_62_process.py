def process(self, string_list):
    """
    'a', 'an', 'the' सहित एक स्टॉप वर्ड सूची बनाएं, और स्ट्रिंग्स की सूची से सभी स्टॉप वर्ड हटा दें।
    :param string_list: स्ट्रिंग्स की एक सूची
    :return: बिना स्टॉप वर्ड के शब्दों की एक सूची
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