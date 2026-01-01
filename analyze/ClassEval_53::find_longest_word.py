def find_longest_word(self, sentence):
    """
        Rimuove i segni di punteggiatura e suddivide una frase in un elenco di parole. Trova la parola suddivisa più lunga che si trova in self.word_list.
        Le parole sono strettamente sensibili al maiuscolo/minuscolo.
        :param sentence: una frase str
        :return str: la parola suddivisa più lunga che si trova in self.word_list. restituisce '' se self.word_list è vuota.
        >>> longestWord = LongestWord()
        >>> longestWord.add_word('A')
        >>> longestWord.add_word('aM')
        >>> longestWord.find_longest_word('I am a student.')
        'a'
        """
    if not self.word_list:
        return ''
    translator = str.maketrans('', '', string.punctuation)
    clean_sentence = sentence.translate(translator)
    words = clean_sentence.split()
    longest_word = ''
    for word in words:
        if word in self.word_list and len(word) > len(longest_word):
            longest_word = word
    return longest_word