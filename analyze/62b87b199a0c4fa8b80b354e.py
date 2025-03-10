def is_fill_request_seq(seq):
    """
    检查 seq 是否可以转换为 FillRequestSeq，并返回布尔值。
    测试 *seq* 是否可以转换为 FillRequestSeq。

    仅当以下条件时返回真：
    - 它是一个 FillRequest 元素，或者包含至少一个 FillRequest 元素；
    - 它不是一个 Source 序列。
    """
    # 假设 FillRequest 和 Source 是某种类型的类或对象
    # 这里我们假设 FillRequest 和 Source 是类的实例
    # 你需要根据实际情况实现这些类的定义
    
    # 检查 seq 是否是 FillRequest 的实例
    if isinstance(seq, FillRequest):
        return True
    
    # 检查 seq 是否是一个序列，并且包含至少一个 FillRequest 元素
    if isinstance(seq, (list, tuple)):
        return any(isinstance(item, FillRequest) for item in seq)
    
    # 检查 seq 是否是 Source 的实例
    if isinstance(seq, Source):
        return False
    
    # 其他情况返回 False
    return False