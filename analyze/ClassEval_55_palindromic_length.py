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
    left = center - diff
    right = center + diff
    
    # 如果超出字符串边界，返回0
    if left < 0 or right >= len(string):
        return 0
    
    # 如果左右字符不相等，返回0
    if string[left] != string[right]:
        return 0
    
    # 如果左右字符相等，递归检查下一层，并加1
    return 1 + self.palindromic_length(center, diff + 1, string)