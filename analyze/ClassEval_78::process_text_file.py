def process_text_file(self, sentences_string):
    """
        Given a text, return the number of words in the longest sentence
        :param sentences_string: string, undivided long sentence
        :return:int, the number of words in the longest sentence
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