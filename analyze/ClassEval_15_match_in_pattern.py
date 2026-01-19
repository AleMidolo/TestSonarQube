def match_in_pattern(self, char):
    """
    Encuentra la ocurrencia más a la derecha de un carácter en el patrón.
    :param char: El carácter que se va a buscar, str.
    :return: El índice de la ocurrencia más a la derecha del carácter en el patrón, int.
    >>> boyerMooreSearch = BoyerMooreSearch("ABAABA", "AB")
    >>> boyerMooreSearch.match_in_pattern("A")
    0

    """
    # Buscar la ocurrencia más a la derecha del carácter en el patrón
    # Recorremos el patrón de derecha a izquierda (excluyendo la última posición)
    for i in range(len(self.pattern) - 2, -1, -1):
        if self.pattern[i] == char:
            return i
    
    # Si no se encuentra el carácter, retornar -1
    return -1