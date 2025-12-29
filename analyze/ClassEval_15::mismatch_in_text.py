def mismatch_in_text(self, currentPos):
    """
        确定模式与文本之间的第一个不匹配的位置。
        :param currentPos: 文本中的当前位置，int。
        :return: 模式与文本之间的第一个不匹配的位置，int，否则返回 -1。
        >>> boyerMooreSearch = BoyerMooreSearch("ABAABA", "ABC")
        >>> boyerMooreSearch.mismatch_in_text(0)
        2
        """
    for j in range(self.patLen - 1, -1, -1):
        if currentPos + j >= self.textLen or self.text[currentPos + j] != self.pattern[j]:
            return j
    return -1