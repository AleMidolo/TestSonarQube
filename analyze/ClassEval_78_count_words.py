def count_words(self, sentence):
    """
    Conta il numero di parole in una frase. Nota che le parole sono separate da spazi e che i segni di punteggiatura e i numeri non sono conteggiati come parole.
    :param sentence:string, frase da contare, dove le parole sono separate da spazi
    :return:int, numero di parole nella frase
    >>> ss.count_words("abc def")
    2
    """
    if not sentence:
        return 0
    
    words = sentence.split()
    count = 0
    
    for word in words:
        # Rimuovi la punteggiatura e controlla se rimane qualcosa di alfabetico
        cleaned_word = ''.join(char for char in word if char.isalpha())
        if cleaned_word:
            count += 1
    
    return count