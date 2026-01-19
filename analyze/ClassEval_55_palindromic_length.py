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
    # Base case: se gli indici sono fuori dai limiti della stringa
    if center - diff < 0 or center + diff >= len(string):
        return 0
    
    # Se i caratteri alle posizioni simmetriche rispetto al centro sono uguali
    if string[center - diff] == string[center + diff]:
        # Incrementa la lunghezza e continua ricorsivamente
        return 1 + self.palindromic_length(center, diff + 1, string)
    else:
        # Se non sono uguali, termina la ricorsione
        return 0