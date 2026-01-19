def match_in_pattern(self, char):
    """
    查找字符在模式中最右侧的出现位置。
    :param char: 要查找的字符，str。
    :return: 该字符在模式串中最右侧出现的索引，int。
    >>> boyerMooreSearch = BoyerMooreSearch("ABAABA", "AB")
    >>> boyerMooreSearch.match_in_pattern("A")
    0

    """
    # 从模式串的右侧向左侧查找字符最后一次出现的位置
    for i in range(len(self.pattern) - 1, -1, -1):
        if self.pattern[i] == char:
            return i
    # 如果字符不在模式串中，返回-1
    return -1