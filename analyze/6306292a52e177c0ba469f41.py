def test_tag(tag: str) -> bool:
    """
    检查 `LEGAL_TAG_CHARS` 中的每个字符是否属于标签。如果有任何字符属于标签，则返回假。否则，返回真。

    测试一个单词是否可以被接受为标签。
    """
    LEGAL_TAG_CHARS = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-")  # 示例合法字符
    return all(char not in tag for char in LEGAL_TAG_CHARS)