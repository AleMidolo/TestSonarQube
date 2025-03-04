def _get_seq_with_type(seq, bufsize=None):
    """
    返回一个 (sequence, type) 对。
    sequence 是从 *seq* 派生的
    （或者是 *seq* 本身，如果它是一个序列类型）。
    """
    # 检查是否为序列类型
    if isinstance(seq, (list, tuple, bytes, bytearray)):
        return seq, type(seq)
    
    # 如果是迭代器或生成器,转换为列表
    if hasattr(seq, '__iter__'):
        if bufsize is None:
            return list(seq), list
        else:
            # 如果指定了bufsize,只获取指定长度
            return [next(iter(seq)) for _ in range(bufsize)], list
            
    # 如果不是序列类型或迭代器,包装成列表
    return [seq], list