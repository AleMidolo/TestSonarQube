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
    left = center - diff
    right = center + diff
    while left >= 0 and right < len(string) and (string[left] == string[right]):
        diff += 1
        left -= 1
        right += 1
    return diff - 1