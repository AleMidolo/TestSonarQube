def bad_character_heuristic(self):
    """
        पाठ में पैटर्न की सभी उपस्थिति को खोजता है।
        :return: पाठ में पैटर्न के सभी स्थानों की एक सूची, सूची।
        >>> boyerMooreSearch = BoyerMooreSearch("ABAABA", "AB")
        >>> boyerMooreSearch.bad_character_heuristic()
        [0, 3]

        """
    if self.patLen == 0:
        return []
    positions = []
    s = 0
    while s <= self.textLen - self.patLen:
        mismatch_pos = self.mismatch_in_text(s)
        if mismatch_pos == -1:
            positions.append(s)
            s += 1
        else:
            bad_char = self.text[mismatch_pos]
            rightmost_pos = self.match_in_pattern(bad_char)
            if rightmost_pos == -1:
                s = mismatch_pos + 1
            else:
                pattern_index = mismatch_pos - s
                shift = max(1, pattern_index - rightmost_pos)
                s += shift
    return positions