def mismatch_in_text(self, currentPos):
    """
    Determina la posición de la primera discrepancia entre el patrón y el texto.
    :param currentPos: La posición actual en el texto, int.
    :return: La posición de la primera discrepancia entre el patrón y el texto, int, de lo contrario -1.
    >>> boyerMooreSearch = BoyerMooreSearch("ABAABA", "ABC")
    >>> boyerMooreSearch.mismatch_in_text(0)
    2

    """
    # Comparar el patrón con el texto desde la posición actual
    # En Boyer-Moore, típicamente comparamos de derecha a izquierda
    for i in range(len(self.pattern) - 1, -1, -1):
        # Verificar que no nos salgamos de los límites del texto
        if currentPos + i >= len(self.text):
            return i
        
        # Si encontramos una discrepancia, retornar la posición en el patrón
        if self.pattern[i] != self.text[currentPos + i]:
            return i
    
    # Si no hay discrepancia, retornar -1 (coincidencia completa)
    return -1