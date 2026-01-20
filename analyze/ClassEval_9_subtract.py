@staticmethod
def subtract(num1, num2):
    """
    Resta dos números grandes.
    :param num1: El primer número a restar, str.
    :param num2: El segundo número a restar, str.
    :return: La diferencia de los dos números, str.
    >>> bigNum = BigNumCalculator()
    >>> bigNum.subtract("12345678901234567890", "98765432109876543210")
    '-86419753208641975320'

    """
    # Handle signs
    negative1 = num1.startswith('-')
    negative2 = num2.startswith('-')
    
    if negative1:
        num1 = num1[1:]
    if negative2:
        num2 = num2[1:]
    
    # Convert subtraction to addition when dealing with negative numbers
    # a - b = a + (-b)
    # a - (-b) = a + b
    # -a - b = -(a + b)
    # -a - (-b) = -a + b = b - a
    
    if negative1 and negative2:
        # -a - (-b) = b - a
        return subtract(num2, num1)
    elif negative1:
        # -a - b = -(a + b)
        result = add(num1, num2)
        return '-' + result if result != '0' else '0'
    elif negative2:
        # a - (-b) = a + b
        return add(num1, num2)
    
    # Both positive: a - b
    # Determine which is larger
    if len(num1) > len(num2):
        is_negative = False
    elif len(num1) < len(num2):
        is_negative = True
        num1, num2 = num2, num1
    else:
        if num1 >= num2:
            is_negative = False
        else:
            is_negative = True
            num1, num2 = num2, num1
    
    # Perform subtraction (num1 - num2, where num1 >= num2)
    result = []
    borrow = 0
    
    # Pad num2 with zeros
    num2 = num2.zfill(len(num1))
    
    for i in range(len(num1) - 1, -1, -1):
        digit1 = int(num1[i])
        digit2 = int(num2[i])
        
        diff = digit1 - digit2 - borrow
        
        if diff < 0:
            diff += 10
            borrow = 1
        else:
            borrow = 0
        
        result.append(str(diff))
    
    # Reverse and remove leading zeros
    result.reverse()
    result_str = ''.join(result).lstrip('0')
    
    if not result_str:
        result_str = '0'
    
    if is_negative and result_str != '0':
        result_str = '-' + result_str
    
    return result_str


def add(num1, num2):
    """Helper function to add two positive number strings"""
    if len(num1) < len(num2):
        num1, num2 = num2, num1
    
    num2 = num2.zfill(len(num1))
    
    result = []
    carry = 0
    
    for i in range(len(num1) - 1, -1, -1):
        digit_sum = int(num1[i]) + int(num2[i]) + carry
        result.append(str(digit_sum % 10))
        carry = digit_sum // 10
    
    if carry:
        result.append(str(carry))
    
    result.reverse()
    return ''.join(result)