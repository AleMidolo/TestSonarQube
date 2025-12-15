def split_sentences(self, text):
        """
        将文本分割成一个句子列表，除了最后一个句子外不带标点符号
        :param text: 要分割的文本
        :return: 分割后的文本列表
        >>> ru = RegexUtils()
        >>> ru.split_sentences("Aaa. Bbbb? Ccc!")
        ['Aaa', 'Bbbb', 'Ccc!']
        """
        pattern = self.generate_split_sentences_pattern()
        sentences = re.split(pattern, text)
        return [sentence.strip() for sentence in sentences if sentence]