def find_longest_word(self, sentence):
    """
    Remove punctuation marks and split a sentence into a list of word. Find the longest splited word that is in the self.word_list.
    Words are strictly case sensitive.
    :param sentence: a sentence str
    :return str: longest splited word that is in the self.word_list. return '' if self.word_list is empty.
    >>> longestWord = LongestWord()
    >>> longestWord.add_word('A')
    >>> longestWord.add_word('aM')
    >>> longestWord.find_longest_word('I am a student.')
    'a'
    """
    import string
    
    # Return empty string if word_list is empty
    if not self.word_list:
        return ''
    
    # Remove punctuation marks from the sentence
    translator = str.maketrans('', '', string.punctuation)
    cleaned_sentence = sentence.translate(translator)
    
    # Split the sentence into words
    words = cleaned_sentence.split()
    
    # Find the longest word that is in self.word_list
    longest_word = ''
    for word in words:
        if word in self.word_list and len(word) > len(longest_word):
            longest_word = word
    
    return longest_word