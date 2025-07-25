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
    
    # 处理0的特殊情况
    if number == 0:
        result = [alphabet[0]]
    else:
        # 将数字转换为字符串
        while number:
            result.append(alphabet[number % base])
            number //= base
        
        # 反转列表以得到正确的顺序
        result.reverse()
    
    # 如果指定了padding，进行填充
    if padding is not None:
        while len(result) < padding:
            result.insert(0, alphabet[0])
    
    return ''.join(result)