def test_tag(tag: str) -> bool:
    """
    检查 `LEGAL_TAG_CHARS` 中的每个字符是否属于标签。如果有任何字符属于标签，则返回假。否则，返回真。

    测试一个单词是否可以被接受为标签。
    """
    LEGAL_TAG_CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_"
    
    # 检查tag中的每个字符
    for char in tag:
        # 如果字符不在合法字符集中,返回False
        if char not in LEGAL_TAG_CHARS:
            return False
            
    # 所有字符都合法,返回True
    return True