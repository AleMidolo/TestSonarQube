def mismatch_in_text(self, currentPos):
    """
        Determines the position of the first dismatch between the pattern and the text.
        :param currentPos: The current position in the text, int.
        :return: The position of the first dismatch between the pattern and the text, int, otherwise -1.
        >>> boyerMooreSearch = BoyerMooreSearch("ABAABA", "ABC")
        >>> boyerMooreSearch.mismatch_in_text(0)
        2
        """
    for j in range(self.patLen - 1, -1, -1):
        if currentPos + j >= self.textLen or self.pattern[j] != self.text[currentPos + j]:
            return j
    return -1