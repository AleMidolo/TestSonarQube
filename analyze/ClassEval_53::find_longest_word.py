def find_longest_word(self, sentence):
    """
        Elimina los signos de puntuación y divide una oración en una lista de palabras. Encuentra la palabra más larga que esté en self.word_list.
        Las palabras son estrictamente sensibles a mayúsculas y minúsculas.
        :param sentence: una oración str
        :return str: la palabra más larga que esté en self.word_list. devuelve '' si self.word_list está vacío.
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