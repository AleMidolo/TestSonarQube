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
    
    # Reverse to get the most significant digit first
    result.reverse()
    
    # Convert list to string
    result_str = ''.join(result)
    
    # Apply padding if necessary
    if padding is not None:
        result_str = result_str.rjust(padding, alphabet[0])
    
    return result_str