def bad_character_heuristic(self):
    """
    在文本中查找模式的所有出现位置。
    :return: 模式在文本中的所有位置的列表,列表。
    >>> boyerMooreSearch = BoyerMooreSearch("ABAABA", "AB")
    >>> boyerMooreSearch.bad_character_heuristic()
    [0, 3]
    """
    text = self.text
    pattern = self.pattern
    m = len(pattern)
    n = len(text)
    
    if m == 0 or n == 0 or m > n:
        return []
    
    # 构建坏字符表
    bad_char = {}
    for i in range(m - 1):
        bad_char[pattern[i]] = m - 1 - i
    
    # 搜索所有匹配位置
    result = []
    s = 0  # s是模式相对于文本的偏移量
    
    while s <= n - m:
        j = m - 1
        
        # 从右向左比较
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1
        
        if j < 0:
            # 找到匹配
            result.append(s)
            s += 1
        else:
            # 发生不匹配,使用坏字符规则
            bad_char_shift = bad_char.get(text[s + j], m)
            s += max(1, bad_char_shift)
    
    return result