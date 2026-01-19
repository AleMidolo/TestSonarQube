def is_valid_input(self, textnum):
    """
        Check if the input text contains only valid words that can be converted into numbers.
        :param textnum: The input text containing words representing numbers.
        :return: True if input is valid, False otherwise.
        >>> w2n = Words2Numbers()
        >>> w2n.is_valid_input("thirty-two")
        False
        """
    textnum = textnum.replace('-', ' ')
    words = textnum.split()
    if not words:
        return False
    for word in words:
        if word in self.ordinal_words:
            continue
        is_ordinal = False
        for ending, replacement in self.ordinal_endings:
            if word.endswith(ending):
                base_word = word[:-len(ending)] + replacement
                if base_word in self.numwords:
                    is_ordinal = True
                    break
        if is_ordinal:
            continue
        if word not in self.numwords:
            return False
    return True