def remove_punctuation(self, sentence):
    """
        从输入文本中移除标点符号。
        :param sentence: 一个句子，str
        :return: str，去除所有标点符号的句子
        >>> lemmatization = Lemmatization()
        >>> lemmatization.remove_punctuation("I am running in a race.")
        'I am running in a race'
        """
    translator = str.maketrans('', '', string.punctuation)
    return sentence.translate(translator)