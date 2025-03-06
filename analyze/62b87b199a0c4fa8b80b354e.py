def is_fill_request_seq(seq):
    """
    检查 seq 是否可以转换为 FillRequestSeq，并返回布尔值。
    测试 *seq* 是否可以转换为 FillRequestSeq。

    仅当以下条件时返回真：
    - 它是一个 FillRequest 元素，或者包含至少一个 FillRequest 元素；
    - 它不是一个 Source 序列。
    """
    # 假设 FillRequest 和 Source 是自定义类
    from collections.abc import Sequence

    # 检查是否是 FillRequest 元素
    if isinstance(seq, FillRequest):
        return True

    # 检查是否是序列且包含至少一个 FillRequest 元素
    if isinstance(seq, Sequence) and not isinstance(seq, Source):
        return any(isinstance(item, FillRequest) for item in seq)

    return False