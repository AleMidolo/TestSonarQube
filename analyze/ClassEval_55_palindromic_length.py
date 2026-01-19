def palindromic_length(self, center, diff, string):
    """
    Calcola ricorsivamente la lunghezza della sottostringa palindromica basata su un centro dato, un valore di differenza e una stringa di input.
    :param center: Il centro della sottostringa palindromica, int.
    :param diff: La differenza tra il centro e la posizione attuale, int.
    :param string: La stringa da cercare, str.
    :return: La lunghezza della sottostringa palindromica, int.
    >>> manacher = Manacher('ababa')
    >>> manacher.palindromic_length(2, 1, 'a|b|a|b|a')
    2

    """
    # Base case: check if indices are within bounds
    if center - diff < 0 or center + diff >= len(string):
        return 0
    
    # Check if characters at symmetric positions match
    if string[center - diff] == string[center + diff]:
        # Recursively expand and add 2 (one for each matching character)
        return 2 + self.palindromic_length(center, diff + 1, string)
    else:
        # Characters don't match, stop expansion
        return 0