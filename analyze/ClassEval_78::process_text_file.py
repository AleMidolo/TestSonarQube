def process_text_file(self, sentences_string):
    """
        Dato un testo, restituisce il numero di parole nella frase più lunga
        :param sentences_string: stringa, frase lunga non divisa
        :return:int, il numero di parole nella frase più lunga
        >>> ss = SplitSentence()
        >>> ss.process_text_file("aaa aaaa. bb bbbb bbb? cccc ccccccc cc ccc. dd ddd?")
        4
        """
    sentences = self.split_sentences(sentences_string)
    max_words = 0
    for sentence in sentences:
        word_count = self.count_words(sentence)
        if word_count > max_words:
            max_words = word_count
    return max_words