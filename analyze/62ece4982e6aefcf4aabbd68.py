from typing import List, Optional

def int_to_string(number: int, alphabet: List[str], padding: Optional[int] = None) -> str:
    """
    将一个数字使用给定的字母表转换为字符串。

      数字表示一个短的 UUID。

      输出的字符串以最高有效位（Most Significant Digit）优先。

      @param number: 整型值  
      @param alphabet: 包含字母的列表  
      @param padding: 可选参数，整型值，用于指定填充长度  
      @return: 与整型值对应的字符串值
    将一个数字转换为字符串，使用给定的字母表。

    输出的字符串以最高有效位优先。
    """
    base = len(alphabet)
    result = []

    if number == 0:
        result.append(alphabet[0])

    while number > 0:
        result.append(alphabet[number % base])
        number //= base

    result.reverse()

    if padding is not None:
        result = ([''] * (padding - len(result))) + result

    return ''.join(result)