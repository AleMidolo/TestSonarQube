def process(self, string_list):
    """
    Construct a stop word list including 'a', 'an', 'the', and remove all the stop words from the list of strings.
    :param string_list: a list of strings
    :return: a list of words without stop words
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