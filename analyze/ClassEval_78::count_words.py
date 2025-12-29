def count_words(self, sentence):
    """
        Count the number of words in a sentence. Note that words are separated by spaces and that punctuation marks and numbers are not counted as words.
        :param sentence:string, sentence to be counted, where words are separated by spaces
        :return:int, number of words in the sentence
        >>> ss.count_words("abc def")
        2
        """
    words = re.sub('[^\\w\\s]', '', sentence).split()
    valid_words = [word for word in words if not word.isdigit()]
    return len(valid_words)