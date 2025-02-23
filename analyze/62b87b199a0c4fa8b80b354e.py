def is_fill_request_seq(seq):
    """
    检查 seq 是否可以转换为 FillRequestSeq，并返回布尔值。
    测试 *seq* 是否可以转换为 FillRequestSeq。

    仅当以下条件时返回真：
    - 它是一个 FillRequest 元素，或者包含至少一个 FillRequest 元素；
    - 它不是一个 Source 序列。
    """
    if isinstance(seq, Source):
        return False
    
    contains_fill_request = any(isinstance(item, FillRequest) for item in seq)
    
    return contains_fill_request or isinstance(seq, FillRequest)