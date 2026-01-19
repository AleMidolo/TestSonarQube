def add_word(self, word):
    """
    将输入的单词添加到 self.word_list 中
    :param word: str，输入的单词
    """
    if not hasattr(self, 'word_list'):
        self.word_list = []
    self.word_list.append(word)