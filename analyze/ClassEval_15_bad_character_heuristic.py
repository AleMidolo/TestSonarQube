def bad_character_heuristic(self):
    """
    在文本中查找模式的所有出现位置。
    :return: 模式在文本中的所有位置的列表,列表。
    >>> boyerMooreSearch = BoyerMooreSearch("ABAABA", "AB")
    >>> boyerMooreSearch.bad_character_heuristic()
    [0, 3]
    """
    result = []
    text = self.text
    pattern = self.pattern
    m = len(pattern)
    n = len(text)
    
    if m == 0 or n == 0 or m > n:
        return result
    
    # 构建坏字符表
    bad_char = {}
    for i in range(m):
        bad_char[pattern[i]] = i
    
    # 搜索过程
    s = 0  # s是模式相对于文本的偏移量
    while s <= n - m:
        j = m - 1
        
        # 从右向左匹配模式
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1
        
        if j < 0:
            # 找到匹配
            result.append(s)
            # 移动到下一个可能的位置
            if s + m < n:
                s += m - bad_char.get(text[s + m], -1)
            else:
                s += 1
        else:
            # 发生不匹配,使用坏字符规则
            bad_char_shift = j - bad_char.get(text[s + j], -1)
            s += max(1, bad_char_shift)
    
    return result