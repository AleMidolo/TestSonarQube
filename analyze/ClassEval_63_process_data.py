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
        # Mantiene solo lettere inglesi e spazi
        filtered_string = ''.join(char for char in string if char.isalpha() or char.isspace())
        # Converte in minuscolo
        lowercase_string = filtered_string.lower()
        # Divide in parole
        words = lowercase_string.split()
        words_list.append(words)
    return words_list