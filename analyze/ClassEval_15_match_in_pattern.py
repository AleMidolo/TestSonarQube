def match_in_pattern(self, char):
    """
    Finds the rightmost occurrence of a character in the pattern.
    :param char: The character to be searched for, str.
    :return: The index of the rightmost occurrence of the character in the pattern, int.
    >>> boyerMooreSearch = BoyerMooreSearch("ABAABA", "AB")
    >>> boyerMooreSearch.match_in_pattern("A")
    0

    """
    # Search from right to left in the pattern
    for i in range(len(self.pattern) - 1, -1, -1):
        if self.pattern[i] == char:
            return i
    # If character not found, return -1
    return -1