def _get_seq_with_type(seq, bufsize=None):
    """
    返回一个 (sequence, type) 对。
    sequence 是从 *seq* 派生的
    （或者是 *seq* 本身，如果它是一个序列类型）。
    """
    if isinstance(seq, (list, tuple, str, bytes, bytearray)):
        return seq, type(seq)
    else:
        # 假设 seq 是一个可迭代对象，但不是序列类型
        # 将其转换为列表
        return list(seq), type(seq)