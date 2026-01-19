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
    while center - diff >= 0 and center + diff < len(string) and (string[center - diff] == string[center + diff]):
        diff += 1
    return diff - 1