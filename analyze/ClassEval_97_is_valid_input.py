def is_valid_input(self, textnum):
    """
        Check if the input text contains only valid words that can be converted into numbers.
        :param textnum: The input text containing words representing numbers.
        :return: True if input is valid, False otherwise.
        >>> w2n = Words2Numbers()
        >>> w2n.is_valid_input("thirty-two")
        False
        """
    valid_words = set(self.numwords.keys()).union(set(self.ordinal_words.keys()))
    words = textnum.replace('-', ' ').split()
    return all((word in valid_words for word in words))