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
    result = []
    
    # 构建坏字符表
    bad_char = {}
    for i in range(m):
        bad_char[pattern[i]] = i
    
    # 搜索过程
    s = 0  # s是模式相对于文本的偏移量
    while s <= n - m:
        j = m - 1
        
        # 从右向左比较模式和文本
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1
        
        # 如果模式完全匹配
        if j < 0:
            result.append(s)
            # 移动模式,使下一个字符对齐
            s += m - bad_char.get(text[s + m], -1) if s + m < n else 1
        else:
            # 使用坏字符规则计算移动距离
            bad_char_shift = j - bad_char.get(text[s + j], -1)
            s += max(1, bad_char_shift)
    
    return result