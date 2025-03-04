def string_to_int(string: str, alphabet: List[str]) -> int:
    """
    将一个数字使用给定的字母表转换为字符串。
    :param string: 一个由字母表中的字母组成的字符串
    :param alphabet: 字母表
    :return: int，使用给定转换规则得到的字符串对应的数字

    假定输入的最高有效位在最前面。
    """
    base = len(alphabet)
    result = 0
    
    # 创建字母到数字的映射
    char_to_num = {char: i for i, char in enumerate(alphabet)}
    
    # 从左到右遍历字符串的每个字符
    for char in string:
        # 将结果乘以进制数,并加上当前字符对应的数值
        result = result * base + char_to_num[char]
        
    return result