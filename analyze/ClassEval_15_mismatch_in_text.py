def mismatch_in_text(self, currentPos):
    """
    Determina la posizione della prima discrepanza tra il pattern e il testo.
    :param currentPos: La posizione attuale nel testo, int.
    :return: La posizione della prima discrepanza tra il modello e il testo, int, altrimenti -1.
    >>> boyerMooreSearch = BoyerMooreSearch("ABAABA", "ABC")
    >>> boyerMooreSearch.mismatch_in_text(0)
    2

    """
    # Confronta il pattern con il testo partendo dalla fine del pattern
    # (Boyer-Moore confronta da destra a sinistra)
    for i in range(len(self.pattern) - 1, -1, -1):
        # Verifica se siamo ancora dentro i limiti del testo
        if currentPos + i >= len(self.text):
            return i
        
        # Se troviamo una discrepanza, restituiamo la posizione nel pattern
        if self.pattern[i] != self.text[currentPos + i]:
            return i
    
    # Se non ci sono discrepanze, restituiamo -1
    return -1