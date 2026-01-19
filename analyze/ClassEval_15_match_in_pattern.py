def match_in_pattern(self, char):
    """
        查找字符在模式中最右侧的出现位置。
        :param char: 要查找的字符，str。
        :return: 该字符在模式串中最右侧出现的索引，int。
        >>> boyerMooreSearch = BoyerMooreSearch("ABAABA", "AB")
        >>> boyerMooreSearch.match_in_pattern("A")
        0
        """
    for i in range(len(self.pattern) - 1, -1, -1):
        if self.pattern[i] == char:
            return i
    return -1