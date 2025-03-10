def is_fill_request_seq(seq):
    """
    检查 seq 是否可以转换为 FillRequestSeq，并返回布尔值。
    测试 *seq* 是否可以转换为 FillRequestSeq。

    仅当以下条件时返回真：
    - 它是一个 FillRequest 元素，或者包含至少一个 FillRequest 元素；
    - 它不是一个 Source 序列。
    """
    # 假设 FillRequest 和 Source 是类或类型
    from typing import Sequence, Type

    FillRequest = Type('FillRequest')  # 假设 FillRequest 是一个类型
    Source = Type('Source')  # 假设 Source 是一个类型

    if isinstance(seq, Source):
        return False

    if isinstance(seq, FillRequest):
        return True

    if isinstance(seq, Sequence):
        return any(isinstance(item, FillRequest) for item in seq)

    return False