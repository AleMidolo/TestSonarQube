def mismatch_in_text(self, currentPos):
    """
    Determines the position of the first dismatch between the pattern and the text.
    :param currentPos: The current position in the text, int.
    :return: The position of the first dismatch between the pattern and the text, int,otherwise -1.
    >>> boyerMooreSearch = BoyerMooreSearch("ABAABA", "ABC")
    >>> boyerMooreSearch.mismatch_in_text(0)
    2

    """
    # Compare pattern with text starting from the end of the pattern
    for i in range(len(self.pattern) - 1, -1, -1):
        # Check if we're within bounds of the text
        if currentPos + i >= len(self.text):
            return i
        # Check if there's a mismatch
        if self.text[currentPos + i] != self.pattern[i]:
            return i
    # No mismatch found, pattern matches completely
    return -1