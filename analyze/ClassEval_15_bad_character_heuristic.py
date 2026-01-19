def bad_character_heuristic(self):
    """
        पाठ में पैटर्न की सभी उपस्थिति को खोजता है।
        :return: पाठ में पैटर्न के सभी स्थानों की एक सूची, सूची।
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
            shift = max(1, mismatchPos - currentPos - badCharIndex)
            currentPos += shift
    return positions