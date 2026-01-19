def add(num1, num2):
    """
    Adds two big numbers.
    :param num1: The first number to add,str.
    :param num2: The second number to add,str.
    :return: The sum of the two numbers,str.
    >>> bigNum = BigNumCalculator()
    >>> bigNum.add("12345678901234567890", "98765432109876543210")
    '111111111011111111100'

    """
    # Make num1 the longer number
    if len(num1) < len(num2):
        num1, num2 = num2, num1
    
    # Pad num2 with leading zeros to match length
    num2 = num2.zfill(len(num1))
    
    result = []
    carry = 0
    
    # Add from right to left
    for i in range(len(num1) - 1, -1, -1):
        digit_sum = int(num1[i]) + int(num2[i]) + carry
        result.append(str(digit_sum % 10))
        carry = digit_sum // 10
    
    # Add remaining carry if any
    if carry:
        result.append(str(carry))
    
    # Reverse to get the correct order
    return ''.join(reversed(result))