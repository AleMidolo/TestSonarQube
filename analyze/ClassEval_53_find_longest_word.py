def find_longest_word(self, sentence):
    """
        移除标点符号并将句子拆分为单词列表。找到在 self.word_list 中的最长拆分单词。
        单词严格区分大小写。
        :param sentence: 一个句子 str
        :return str: 在 self.word_list 中的最长拆分单词。如果 self.word_list 为空，则返回 ''。
        >>> longestWord = LongestWord()
        >>> longestWord.add_word('A')
        >>> longestWord.add_word('aM')
        >>> longestWord.find_longest_word('I am a student.')
        'a'
        """
    words = re.findall('\\b\\w+\\b', sentence)
    if not self.word_list:
        return ''
    longest = ''
    for word in words:
        if word in self.word_list and len(word) > len(longest):
            longest = word
    return longest