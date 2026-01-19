def add(num1, num2):
    """
    दो बड़े नंबर जोड़ता है।
    :param num1: जोड़ने के लिए पहला नंबर, str.
    :param num2: जोड़ने के लिए दूसरा नंबर, str.
    :return: दोनों नंबरों का योग, str.
    >>> bigNum = BigNumCalculator()
    >>> bigNum.add("12345678901234567890", "98765432109876543210")
    '111111111011111111100'

    """
    # Make num1 the longer string
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
    
    # If there's a remaining carry, add it
    if carry:
        result.append(str(carry))
    
    # Reverse the result and join
    return ''.join(reversed(result))