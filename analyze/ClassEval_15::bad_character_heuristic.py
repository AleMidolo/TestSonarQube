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
        j = self.patLen - 1
        while j >= 0 and self.pattern[j] == self.text[s + j]:
            j -= 1
        if j < 0:
            positions.append(s)
            if s + self.patLen < self.textLen:
                char_index = self.match_in_pattern(self.text[s + self.patLen])
                s += self.patLen - char_index if char_index != -1 else self.patLen + 1
            else:
                s += 1
        else:
            char_index = self.match_in_pattern(self.text[s + j])
            s += max(1, j - char_index)
    return positions