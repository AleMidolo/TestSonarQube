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
    
    # Reverse both strings for easier addition from right to left
    num1 = num1[::-1]
    num2 = num2[::-1]
    
    result = []
    carry = 0
    
    # Add digits from both numbers
    for i in range(len(num1)):
        digit1 = int(num1[i])
        digit2 = int(num2[i]) if i < len(num2) else 0
        
        total = digit1 + digit2 + carry
        result.append(str(total % 10))
        carry = total // 10
    
    # Add remaining carry if any
    if carry > 0:
        result.append(str(carry))
    
    # Reverse the result to get the final answer
    return ''.join(result[::-1])