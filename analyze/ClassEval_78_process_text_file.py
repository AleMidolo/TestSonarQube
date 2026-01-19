def process_text_file(self, sentences_string):
    """
        दिए गए पाठ के लिए, सबसे लंबे वाक्य में शब्दों की संख्या लौटाएं
        :param sentences_string: स्ट्रिंग, अविभाजित लंबा वाक्य
        :return:int, सबसे लंबे वाक्य में शब्दों की संख्या
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