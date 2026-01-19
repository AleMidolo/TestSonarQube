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
    import string
    
    # 如果 word_list 为空，返回空字符串
    if not self.word_list:
        return ''
    
    # 移除标点符号
    translator = str.maketrans('', '', string.punctuation)
    cleaned_sentence = sentence.translate(translator)
    
    # 拆分为单词列表
    words = cleaned_sentence.split()
    
    # 找到在 word_list 中的最长单词
    longest_word = ''
    for word in words:
        if word in self.word_list and len(word) > len(longest_word):
            longest_word = word
    
    return longest_word