def bad_character_heuristic(self):
    """
        在文本中查找模式的所有出现位置。
        :return: 模式在文本中的所有位置的列表，列表。
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