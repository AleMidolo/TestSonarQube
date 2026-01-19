def mismatch_in_text(self, currentPos):
    """
    确定模式与文本之间的第一个不匹配的位置。
    :param currentPos: 文本中的当前位置，int。
    :return: 模式与文本之间的第一个不匹配的位置，int，否则返回 -1。
    >>> boyerMooreSearch = BoyerMooreSearch("ABAABA", "ABC")
    >>> boyerMooreSearch.mismatch_in_text(0)
    2

    """
    # 从模式的末尾开始向前比较
    for i in range(len(self.pattern) - 1, -1, -1):
        # 检查文本位置是否越界
        if currentPos + i >= len(self.text):
            return i
        # 如果字符不匹配，返回该位置
        if self.pattern[i] != self.text[currentPos + i]:
            return i
    # 如果所有字符都匹配，返回 -1
    return -1