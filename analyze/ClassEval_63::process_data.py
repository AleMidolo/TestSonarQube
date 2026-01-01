def process_data(self, string_list):
    """
        keep only English letters and spaces in the string, then convert the string to lower case, and then split the string into a list of words.
        :param string_list: a list of strings
        :return: words_list: a list of words lists
        >>> NLPDataProcessor2().process_data(['This is a test.'])
        [['this', 'is', 'a', 'test']]
        """
    words_list = []
    for string in string_list:
        cleaned_string = re.sub('[^a-zA-Z\\s]', '', string)
        cleaned_string = cleaned_string.lower()
        words = [word for word in cleaned_string.split() if word]
        if words:
            words_list.append(words)
    return words_list