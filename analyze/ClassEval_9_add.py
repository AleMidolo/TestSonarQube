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
    # Handle negative numbers
    if num1.startswith('-') and num2.startswith('-'):
        return '-' + add(num1[1:], num2[1:])
    elif num1.startswith('-'):
        return subtract(num2, num1[1:])
    elif num2.startswith('-'):
        return subtract(num1, num2[1:])
    
    # Make sure num1 is the longer number
    if len(num1) < len(num2):
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
    
    # Reverse to get the correct order
    return ''.join(reversed(result))

def subtract(num1, num2):
    """Helper function for handling subtraction in negative cases"""
    # Determine which number is larger
    is_negative = False
    if len(num1) < len(num2) or (len(num1) == len(num2) and num1 < num2):
        num1, num2 = num2, num1
        is_negative = True
    
    # Pad num2 with leading zeros
    num2 = num2.zfill(len(num1))
    
    result = []
    borrow = 0
    
    # Subtract from right to left
    for i in range(len(num1) - 1, -1, -1):
        diff = int(num1[i]) - int(num2[i]) - borrow
        if diff < 0:
            diff += 10
            borrow = 1
        else:
            borrow = 0
        result.append(str(diff))
    
    # Reverse and remove leading zeros
    result_str = ''.join(reversed(result)).lstrip('0')
    if not result_str:
        result_str = '0'
    
    return '-' + result_str if is_negative else result_str