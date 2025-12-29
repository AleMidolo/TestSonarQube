def match_in_pattern(self, char, current_pos_in_pattern):
    """
        Finds the rightmost occurrence of a character in the pattern.
        :param char: The character to be searched for, str.
        :param current_pos_in_pattern: The current position in the pattern where mismatch occurred, int.
        :return: The index of the rightmost occurrence of the character in the pattern, int.
        >>> boyerMooreSearch = BoyerMooreSearch("ABAABA", "AB")
        >>> boyerMooreSearch.match_in_pattern("A", 1)
        0

        """
    for i in range(current_pos_in_pattern - 1, -1, -1):
        if self.pattern[i] == char:
            return i
    return -1