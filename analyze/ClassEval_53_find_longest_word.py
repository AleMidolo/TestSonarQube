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
    if not self.word_list:
        return ''
    words = re.findall('\\b\\w+\\b', sentence)
    longest = ''
    for word in words:
        if word in self.word_list and len(word) > len(longest):
            longest = word
    return longest