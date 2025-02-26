from typing import List

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
    for char in string:
        result = result * base + alphabet.index(char)
    return result