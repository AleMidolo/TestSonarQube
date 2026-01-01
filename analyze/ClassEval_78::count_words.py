def count_words(self, sentence):
    """
        Conta il numero di parole in una frase. Nota che le parole sono separate da spazi e che i segni di punteggiatura e i numeri non sono conteggiati come parole.
        :param sentence:string, frase da contare, dove le parole sono separate da spazi
        :return:int, numero di parole nella frase
        >>> ss = SplitSentence()
        >>> ss.count_words("abc def")
        2
        """
    return len([word for word in sentence.split() if word.isalpha()])