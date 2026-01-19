def add(num1, num2):
    """
    Aggiunge due grandi numeri.
    :param num1: Il primo numero da aggiungere, str.
    :param num2: Il secondo numero da aggiungere, str.
    :return: La somma dei due numeri, str.
    >>> bigNum = BigNumCalculator()
    >>> bigNum.add("12345678901234567890", "98765432109876543210")
    '111111111011111111100'

    """
    # Handle empty strings
    if not num1:
        return num2 if num2 else "0"
    if not num2:
        return num1
    
    # Make sure num1 is the longer number
    if len(num2) > len(num1):
        num1, num2 = num2, num1
    
    # Pad the shorter number with zeros on the left
    num2 = num2.zfill(len(num1))
    
    result = []
    carry = 0
    
    # Add digits from right to left
    for i in range(len(num1) - 1, -1, -1):
        digit_sum = int(num1[i]) + int(num2[i]) + carry
        result.append(str(digit_sum % 10))
        carry = digit_sum // 10
    
    # If there's a remaining carry, add it
    if carry:
        result.append(str(carry))
    
    # Reverse the result to get the correct order
    return ''.join(reversed(result))