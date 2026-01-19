def interpret(self, display=False):
    """
    解析要演奏的乐谱
    :param display: Bool，表示是否打印解析后的乐谱
    :return: dict 的列表，字典包括两个字段，Chord 和 Tune，分别是字母和数字。如果输入为空或仅包含空格，则返回一个空列表。
    >>> context = AutomaticGuitarSimulator("C53231323 Em43231323 F43231323 G63231323")
    >>> play_list = context.interpret(display = False)
    [{'Chord': 'C', 'Tune': '53231323'}, {'Chord': 'Em', 'Tune': '43231323'}, {'Chord': 'F', 'Tune': '43231323'}, {'Chord': 'G', 'Tune': '63231323'}]

    """
    # 如果输入为空或仅包含空格，返回空列表
    if not hasattr(self, 'score') or not self.score or self.score.strip() == '':
        return []
    
    # 分割乐谱字符串
    parts = self.score.split()
    result = []
    
    for part in parts:
        if not part:  # 跳过空字符串
            continue
        
        # 分离和弦（字母部分）和音调（数字部分）
        chord = ''
        tune = ''
        
        for char in part:
            if char.isalpha():
                chord += char
            elif char.isdigit():
                tune += char
        
        # 只有当和弦和音调都存在时才添加到结果中
        if chord and tune:
            result.append({'Chord': chord, 'Tune': tune})
    
    # 如果需要显示，打印解析后的乐谱
    if display:
        print(result)
    
    return result