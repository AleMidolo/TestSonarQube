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
    while center - diff >= 0 and center + diff < len(string) and (string[center - diff] == string[center + diff]):
        diff += 1
    return diff - 1