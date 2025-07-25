def _normalizeargs(sequence, output=None):
    """
    规范化声明参数

    规范化的参数可能包含声明、元组或单个接口。

    除了单个接口或实现规范之外的任何内容都将被展开。
    """
    if output is None:
        output = []
    
    if isinstance(sequence, (list, tuple)):
        for item in sequence:
            _normalizeargs(item, output)
    else:
        if sequence not in output:
            output.append(sequence)
            
    return output