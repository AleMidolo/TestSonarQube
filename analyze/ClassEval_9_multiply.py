@staticmethod
def multiply(num1, num2):
    """
    把两个大数字相乘。
    :param num1: 第一个要相乘的数字，字符串。
    :param num2: 第二个要相乘的数字，字符串。
    :return: 两个数字的乘积，字符串。
    >>> bigNum = BigNumCalculator()
    >>> bigNum.multiply("12345678901234567890", "98765432109876543210")
    '1219326311370217952237463801111263526900'

    """
    # 处理特殊情况
    if num1 == "0" or num2 == "0":
        return "0"
    
    # 判断符号
    negative = False
    if num1[0] == '-':
        negative = not negative
        num1 = num1[1:]
    if num2[0] == '-':
        negative = not negative
        num2 = num2[1:]
    
    # 反转字符串，方便从低位开始计算
    num1 = num1[::-1]
    num2 = num2[::-1]
    
    # 结果数组，最多 len(num1) + len(num2) 位
    result = [0] * (len(num1) + len(num2))
    
    # 逐位相乘
    for i in range(len(num1)):
        for j in range(len(num2)):
            # 当前位相乘
            product = int(num1[i]) * int(num2[j])
            # 加到对应位置
            result[i + j] += product
            # 处理进位
            result[i + j + 1] += result[i + j] // 10
            result[i + j] %= 10
    
    # 移除前导零
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    
    # 反转结果并转换为字符串
    result_str = ''.join(map(str, result[::-1]))
    
    # 添加符号
    if negative:
        result_str = '-' + result_str
    
    return result_str