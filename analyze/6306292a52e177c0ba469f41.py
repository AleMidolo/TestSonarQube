def test_tag(tag: str) -> bool:
    """
    检查 `LEGAL_TAG_CHARS` 中的每个字符是否属于标签。如果有任何字符属于标签，则返回假。否则，返回真。

    测试一个单词是否可以被接受为标签。
    """
    LEGAL_TAG_CHARS = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_")
    
    for char in tag:
        if char not in LEGAL_TAG_CHARS:
            return False
    return True