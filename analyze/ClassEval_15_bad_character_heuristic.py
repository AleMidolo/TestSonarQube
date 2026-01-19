def bad_character_heuristic(self):
    """
        在文本中查找模式的所有出现位置。
        :return: 模式在文本中的所有位置的列表，列表。
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
            badCharIndex = self.match_in_pattern(self.text[mismatchPos])
            shift = max(1, mismatchPos - (currentPos + badCharIndex))
            currentPos += shift
    return positions