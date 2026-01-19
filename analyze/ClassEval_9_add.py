def add(num1, num2):
    """
    把两个大数字相加。
    :param num1: 要相加的第一个数字，字符串。
    :param num2: 要相加的第二个数字，字符串。
    :return: 两个数字的和，字符串。
    >>> bigNum = BigNumCalculator()
    >>> bigNum.add("12345678901234567890", "98765432109876543210")
    '111111111011111111100'

    """
    # 处理空字符串和符号
    if not num1:
        num1 = "0"
    if not num2:
        num2 = "0"
    
    # 反转字符串以便从低位开始相加
    num1 = num1[::-1]
    num2 = num2[::-1]
    
    # 确保num1是较长的数
    if len(num1) < len(num2):
        num1, num2 = num2, num1
    
    result = []
    carry = 0
    
    # 逐位相加
    for i in range(len(num1)):
        digit1 = int(num1[i])
        digit2 = int(num2[i]) if i < len(num2) else 0
        
        total = digit1 + digit2 + carry
        result.append(str(total % 10))
        carry = total // 10
    
    # 处理最后的进位
    if carry:
        result.append(str(carry))
    
    # 反转结果并返回
    return ''.join(result[::-1])