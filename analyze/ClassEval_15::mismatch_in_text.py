def mismatch_in_text(self, currentPos):
    """
        Determines the position of the first dismatch between the pattern and the text.
        :param currentPos: The current position in the text, int.
        :return: The position of the first dismatch between the pattern and the text, int,otherwise -1.
        >>> boyerMooreSearch = BoyerMooreSearch("ABAABA", "ABC")
        >>> boyerMooreSearch.mismatch_in_text(0)
        2

        """
    for i in range(self.patLen - 1, -1, -1):
        if self.text[currentPos + i] != self.pattern[i]:
            return i
    return -1