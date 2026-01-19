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
    import string
    
    # Rimuove i segni di punteggiatura
    translator = str.maketrans('', '', string.punctuation)
    cleaned_sentence = sentence.translate(translator)
    
    # Suddivide la frase in parole
    words = cleaned_sentence.split()
    
    # Trova la parola più lunga che si trova in self.word_list
    longest = ''
    for word in words:
        if word in self.word_list and len(word) > len(longest):
            longest = word
    
    return longest