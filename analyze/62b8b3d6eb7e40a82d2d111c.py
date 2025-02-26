def _normalizeargs(sequence, output=None):
    """
    规范化声明参数


    规范化的参数可能包含声明、元组或单个接口。


    除了单个接口或实现规范之外的任何内容都将被展开。
    """
    if isinstance(sequence, (list, tuple)):
        normalized = []
        for item in sequence:
            if isinstance(item, (list, tuple)):
                normalized.extend(_normalizeargs(item))
            else:
                normalized.append(item)
        return normalized
    elif isinstance(sequence, dict):
        return {key: _normalizeargs(value) for key, value in sequence.items()}
    else:
        return [sequence] if output is None else output