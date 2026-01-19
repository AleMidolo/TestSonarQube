def palindromic_length(self, center, diff, string):
    """
        Calcula recursivamente la longitud de la subcadena palindrómica basada en un centro dado, un valor de diferencia y una cadena de entrada.
        :param center: El centro de la subcadena palindrómica, int.
        :param diff: La diferencia entre el centro y la posición actual, int.
        :param string: La cadena a ser buscada, str.
        :return: La longitud de la subcadena palindrómica, int.
        >>> manacher = Manacher('ababa')
        >>> manacher.palindromic_length(2, 1, 'a|b|a|b|a')
        2
        """
    if center - diff < 0 or center + diff >= len(string):
        return diff - 1
    if string[center - diff] == string[center + diff]:
        return self.palindromic_length(center, diff + 1, string)
    return diff - 1