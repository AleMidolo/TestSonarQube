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
    # 检查边界条件
    if center - diff < 0 or center + diff >= len(string):
        return 0
    
    # 检查当前位置的字符是否相等
    if string[center - diff] == string[center + diff]:
        # 如果相等，递归检查下一层，并返回当前长度加上递归结果
        return 1 + self.palindromic_length(center, diff + 1, string)
    else:
        # 如果不相等，返回0
        return 0