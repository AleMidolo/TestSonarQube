def is_fill_request_seq(seq):
    """
    检查 seq 是否可以转换为 FillRequestSeq，并返回布尔值。
    测试 *seq* 是否可以转换为 FillRequestSeq。

    仅当以下条件时返回真：
    - 它是一个 FillRequest 元素，或者包含至少一个 FillRequest 元素；
    - 它不是一个 Source 序列。
    """
    # 假设 FillRequest 和 Source 是自定义类或类型
    # 这里假设 FillRequest 和 Source 是类的实例或类型
    from typing import Sequence, Type

    # 假设 FillRequest 和 Source 是已知的类型
    FillRequest = Type['FillRequest']
    Source = Type['Source']

    # 检查 seq 是否是 FillRequest 类型
    if isinstance(seq, FillRequest):
        return True

    # 检查 seq 是否是序列类型，并且包含至少一个 FillRequest 元素
    if isinstance(seq, Sequence):
        if any(isinstance(item, FillRequest) for item in seq):
            # 检查 seq 是否是 Source 序列
            if not isinstance(seq, Source):
                return True

    return False