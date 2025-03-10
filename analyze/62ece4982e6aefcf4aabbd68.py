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
    """
    base = len(alphabet)
    result = []
    
    while number > 0:
        remainder = number % base
        result.append(alphabet[remainder])
        number = number // base
    
    # 如果指定了填充长度，并且结果长度小于填充长度，则进行填充
    if padding is not None:
        while len(result) < padding:
            result.append(alphabet[0])
    
    # 反转列表以得到最高有效位优先的字符串
    result.reverse()
    
    return ''.join(result)