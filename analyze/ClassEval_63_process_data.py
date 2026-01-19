def process_data(self, string_list):
    """
    keep only English letters and spaces in the string, then convert the string to lower case, and then split the string into a list of words.
    :param string_list: a list of strings
    :return: words_list: a list of words lists
    >>> NLPDataProcessor.process_data(['This is a test.'])
    [['this', 'is', 'a', 'test']]
    """
    words_list = []
    for string in string_list:
        # Keep only English letters and spaces
        cleaned = ''.join(char if char.isalpha() or char.isspace() else '' for char in string)
        # Convert to lower case
        cleaned = cleaned.lower()
        # Split into words
        words = cleaned.split()
        words_list.append(words)
    return words_list