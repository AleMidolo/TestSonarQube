def process_data(self, string_list):
    """
        mantiene solo le lettere inglesi e gli spazi nella stringa, quindi converte la stringa in minuscolo e poi divide la stringa in una lista di parole.
        :param string_list: una lista di stringhe
        :return: words_list: una lista di liste di parole
        >>> NLPDataProcessor.process_data(['This is a test.'])
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