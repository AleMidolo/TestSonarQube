def count_words(self, sentence):
    """
        计算句子中的单词数量。注意，单词由空格分隔，标点符号和数字不算作单词。
        :param sentence:字符串, 要计算的句子，单词由空格分隔
        :return:int, 句子中的单词数量
        >>> ss.count_words("abc def")
        2
        """
    cleaned = re.sub('[^a-zA-Z\\s]', '', sentence)
    words = [word for word in cleaned.split() if word]
    return len(words)