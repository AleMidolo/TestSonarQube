def bad_character_heuristic(self):
    """
        Finds all occurrences of the pattern in the text.
        :return: A list of all positions of the pattern in the text, list.
        >>> boyerMooreSearch = BoyerMooreSearch("ABAABA", "AB")
        >>> boyerMooreSearch.bad_character_heuristic()
        [0, 3]
        """
    positions = []
    skip = 0
    while skip <= self.textLen - self.patLen:
        mismatch_index = self.mismatch_in_text(skip)
        if mismatch_index == -1:
            positions.append(skip)
            skip += self.patLen - self.match_in_pattern(self.text[skip + self.patLen - 1])
        else:
            skip += max(1, mismatch_index - skip)
    return positions