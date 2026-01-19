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
    # 处理空字符串和负数情况
    if not num1:
        num1 = "0"
    if not num2:
        num2 = "0"
    
    # 处理负数
    if num1[0] == '-' and num2[0] == '-':
        # 两个都是负数
        return '-' + add(num1[1:], num2[1:])
    elif num1[0] == '-':
        # num1是负数，num2是正数：num2 - abs(num1)
        return subtract(num2, num1[1:])
    elif num2[0] == '-':
        # num2是负数，num1是正数：num1 - abs(num2)
        return subtract(num1, num2[1:])
    
    # 两个都是正数，进行加法
    # 反转字符串，从低位开始相加
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


def subtract(num1, num2):
    """辅助函数：计算 num1 - num2（假设都是正数字符串）"""
    # 比较大小
    if len(num1) < len(num2) or (len(num1) == len(num2) and num1 < num2):
        # num1 < num2，结果为负
        return '-' + subtract(num2, num1)
    
    # num1 >= num2
    num1 = num1[::-1]
    num2 = num2[::-1]
    
    result = []
    borrow = 0
    
    for i in range(len(num1)):
        digit1 = int(num1[i])
        digit2 = int(num2[i]) if i < len(num2) else 0
        
        diff = digit1 - digit2 - borrow
        if diff < 0:
            diff += 10
            borrow = 1
        else:
            borrow = 0
        
        result.append(str(diff))
    
    # 移除前导零
    while len(result) > 1 and result[-1] == '0':
        result.pop()
    
    return ''.join(result[::-1])