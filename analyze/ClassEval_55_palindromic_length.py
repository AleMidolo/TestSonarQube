def palindromic_length(self, center, diff, string):
    """
    递归计算基于给定中心、差值和输入字符串的回文子串的长度。
    :param center: 回文子串的中心，int。
    :param diff: 中心与当前位之间的差值，int。
    :param string: 要搜索的字符串，str。
    :return: 回文子串的长度，int。
    >>> manacher = Manacher('ababa')
    >>> manacher.palindromic_length(2, 1, 'a|b|a|b|a')
    2

    """
    # Base case: check if indices are within bounds
    if center - diff < 0 or center + diff >= len(string):
        return 0
    
    # Check if characters at center-diff and center+diff are equal
    if string[center - diff] == string[center + diff]:
        # If they match, recursively check the next pair and add 2 to the length
        return 2 + self.palindromic_length(center, diff + 1, string)
    else:
        # If they don't match, return 0 (no more palindrome extension)
        return 0