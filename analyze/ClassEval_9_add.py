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
    # Make sure both numbers have the same length by padding with zeros
    max_len = max(len(num1), len(num2))
    num1 = num1.zfill(max_len)
    num2 = num2.zfill(max_len)
    
    result = []
    carry = 0
    
    # Add from right to left
    for i in range(max_len - 1, -1, -1):
        digit_sum = int(num1[i]) + int(num2[i]) + carry
        result.append(str(digit_sum % 10))
        carry = digit_sum // 10
    
    # If there's a remaining carry, add it
    if carry > 0:
        result.append(str(carry))
    
    # Reverse the result and join to form the final string
    return ''.join(reversed(result))