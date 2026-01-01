def process_text_file(self, sentences_string):
    """
        Given a text, return the number of words in the longest sentence
        :param sentences_string: string, undivided long sentence
        :return:int, the number of words in the longest sentence
        >>> ss = SplitSentence()
        >>> ss.process_text_file("aaa aaaa. bb bbbb bbb? cccc ccccccc cc ccc. dd ddd?")
        4
        """
    sentences = self.split_sentences(sentences_string)
    longest_sentence_length = max((self.count_words(sentence) for sentence in sentences))
    return longest_sentence_length