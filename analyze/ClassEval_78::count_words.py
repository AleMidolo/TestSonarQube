def count_words(self, sentence):
    """
        Conta il numero di parole in una frase. Nota che le parole sono separate da spazi e che i segni di punteggiatura e i numeri non sono conteggiati come parole.
        :param sentence:string, frase da contare, dove le parole sono separate da spazi
        :return:int, numero di parole nella frase
        >>> ss.count_words("abc def")
        2
        """
    words = re.findall('\\b[a-zA-Z]+\\b', sentence)
    return len(words)