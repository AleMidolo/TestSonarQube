def add(num1, num2):
    """
    Suma dos números grandes.
    :param num1: El primer número a sumar, str.
    :param num2: El segundo número a sumar, str.
    :return: La suma de los dos números, str.
    >>> bigNum = BigNumCalculator()
    >>> bigNum.add("12345678901234567890", "98765432109876543210")
    '111111111011111111100'

    """
    # Handle empty strings
    if not num1:
        return num2 if num2 else "0"
    if not num2:
        return num1
    
    # Make num1 the longer number
    if len(num2) > len(num1):
        num1, num2 = num2, num1
    
    # Pad num2 with leading zeros
    num2 = num2.zfill(len(num1))
    
    result = []
    carry = 0
    
    # Add from right to left
    for i in range(len(num1) - 1, -1, -1):
        digit_sum = int(num1[i]) + int(num2[i]) + carry
        result.append(str(digit_sum % 10))
        carry = digit_sum // 10
    
    # Add remaining carry
    if carry:
        result.append(str(carry))
    
    # Reverse to get correct order
    return ''.join(reversed(result))