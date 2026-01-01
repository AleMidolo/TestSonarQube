def match_in_pattern(self, char):
    """
        Trova l'occorrenza più a destra di un carattere nel pattern.
        :param char: Il carattere da cercare, str.
        :return: L'indice dell'occorrenza più a destra del carattere nel pattern, int.
        >>> boyerMooreSearch = BoyerMooreSearch("ABAABA", "AB")
        >>> boyerMooreSearch.match_in_pattern("A")
        0
        """
    for i in range(len(self.pattern) - 1, -1, -1):
        if self.pattern[i] == char:
            return i
    return -1