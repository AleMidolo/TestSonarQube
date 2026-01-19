def process_text_file(self, sentences_string):
    """
        给定一段文本，返回最长句子中的单词数量
        :param sentences_string: 字符串，未分割的长句子
        :return: int，最长句子中的单词数量
        >>> ss.process_text_file("aaa aaaa. bb bbbb bbb? cccc ccccccc cc ccc. dd ddd?")
        4
        """
    sentences = self.split_sentences(sentences_string)
    max_word_count = 0
    for sentence in sentences:
        word_count = self.count_words(sentence)
        if word_count > max_word_count:
            max_word_count = word_count
    return max_word_count