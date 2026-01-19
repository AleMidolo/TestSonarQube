def match_in_pattern(self, char):
    """
    查找字符在模式中最右侧的出现位置。
    :param char: 要查找的字符，str。
    :return: 该字符在模式串中最右侧出现的索引，int。
    >>> boyerMooreSearch = BoyerMooreSearch("ABAABA", "AB")
    >>> boyerMooreSearch.match_in_pattern("A")
    0

    """
    # 从模式串的右侧向左侧查找字符最右侧的出现位置
    # 注意：通常在Boyer-Moore算法中，我们需要找到字符在模式串中从右往左数第一次出现的位置
    # 但不包括模式串的最后一个字符（因为那是当前比较位置）
    
    # 从模式串的倒数第二个位置开始向左查找
    for i in range(len(self.pattern) - 2, -1, -1):
        if self.pattern[i] == char:
            return i
    
    # 如果字符不在模式串中（除了最后一个位置），返回-1
    return -1