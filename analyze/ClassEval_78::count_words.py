def count_words(self, sentence):
    """
        Conta il numero di parole in una frase. Nota che le parole sono separate da spazi e che i segni di punteggiatura e i numeri non sono conteggiati come parole.
        :param sentence:string, frase da contare, dove le parole sono separate da spazi
        :return:int, numero di parole nella frase
        >>> ss.count_words("abc def")
        2
        """
    cleaned_sentence = re.sub('[^\\w\\s]', '', sentence)
    words = cleaned_sentence.split()
    valid_words = [word for word in words if not word.isdigit()]
    return len(valid_words)