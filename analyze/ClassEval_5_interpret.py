def interpret(self, display=False):
    """
    解析要演奏的乐谱
    :param display: Bool，表示是否打印解析后的乐谱
    :return: dict 的列表，字典包括两个字段，Chord 和 Tune，分别是字母和数字。如果输入为空或仅包含空格，则返回一个空列表。
    >>> context = AutomaticGuitarSimulator("C53231323 Em43231323 F43231323 G63231323")
    >>> play_list = context.interpret(display = False)
    [{'Chord': 'C', 'Tune': '53231323'}, {'Chord': 'Em', 'Tune': '43231323'}, {'Chord': 'F', 'Tune': '43231323'}, {'Chord': 'G', 'Tune': '63231323'}]

    """
    # 检查输入是否为空或仅包含空格
    if not hasattr(self, 'score') or not self.score or self.score.strip() == '':
        return []
    
    # 分割乐谱字符串
    parts = self.score.strip().split()
    
    result = []
    
    for part in parts:
        if not part:
            continue
        
        # 找到字母和数字的分界点
        chord = ''
        tune = ''
        
        i = 0
        # 提取和弦部分（字母）
        while i < len(part) and (part[i].isalpha() or part[i] == '#' or part[i] == 'b'):
            chord += part[i]
            i += 1
        
        # 提取音调部分（数字）
        while i < len(part):
            tune += part[i]
            i += 1
        
        # 只有当和弦和音调都存在时才添加到结果中
        if chord and tune:
            result.append({'Chord': chord, 'Tune': tune})
    
    # 如果需要显示，打印解析后的乐谱
    if display:
        print(result)
    
    return result