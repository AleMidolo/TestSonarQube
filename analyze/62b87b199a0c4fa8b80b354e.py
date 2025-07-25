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
    # 并且我们假设 seq 是一个列表或单个对象

    # 检查 seq 是否是单个 FillRequest 对象
    if isinstance(seq, FillRequest):
        return True

    # 检查 seq 是否是一个序列（例如列表）
    if isinstance(seq, (list, tuple)):
        # 检查序列中是否至少有一个 FillRequest 对象
        if any(isinstance(item, FillRequest) for item in seq):
            # 检查序列是否不是 Source 序列
            if not isinstance(seq, Source):
                return True

    return False