def bad_character_heuristic(self):
    """
        Finds all occurrences of the pattern in the text.
        :return: A list of all positions of the pattern in the text, list.
        >>> boyerMooreSearch = BoyerMooreSearch("ABAABA", "AB")
        >>> boyerMooreSearch.bad_character_heuristic()
        [0, 3]

        """
    positions = []
    currentPos = 0
    while currentPos <= self.textLen - self.patLen:
        mismatchPos = self.mismatch_in_text(currentPos)
        if mismatchPos == -1:
            positions.append(currentPos)
            currentPos += 1
        else:
            badChar = self.text[mismatchPos]
            rightmostIndex = self.match_in_pattern(badChar)
            if rightmostIndex == -1:
                currentPos = mismatchPos + 1
            else:
                shift = mismatchPos - (currentPos + rightmostIndex)
                currentPos += max(1, shift)
    return positions