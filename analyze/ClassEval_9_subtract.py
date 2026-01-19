@staticmethod
def subtract(num1, num2):
    """
    Subtracts two big numbers.
    :param num1: The first number to subtract,str.
    :param num2: The second number to subtract,str.
    :return: The difference of the two numbers,str.
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
    
    # Convert subtraction to addition if needed
    # a - b = a + (-b)
    # a - (-b) = a + b
    # -a - b = -(a + b)
    # -a - (-b) = -a + b = b - a
    
    if negative1 and negative2:
        # -a - (-b) = b - a
        return BigNumCalculator.subtract(num2, num1)
    elif negative1:
        # -a - b = -(a + b)
        result = BigNumCalculator.add(num1, num2)
        return '-' + result if result != '0' else '0'
    elif negative2:
        # a - (-b) = a + b
        return BigNumCalculator.add(num1, num2)
    
    # Both positive: num1 - num2
    # Determine which is larger
    if len(num1) > len(num2):
        larger, smaller = num1, num2
        result_negative = False
    elif len(num2) > len(num1):
        larger, smaller = num2, num1
        result_negative = True
    else:
        if num1 >= num2:
            larger, smaller = num1, num2
            result_negative = False
        else:
            larger, smaller = num2, num1
            result_negative = True
    
    # Perform subtraction
    larger = larger[::-1]
    smaller = smaller[::-1]
    
    result = []
    borrow = 0
    
    for i in range(len(larger)):
        digit1 = int(larger[i])
        digit2 = int(smaller[i]) if i < len(smaller) else 0
        
        diff = digit1 - digit2 - borrow
        
        if diff < 0:
            diff += 10
            borrow = 1
        else:
            borrow = 0
        
        result.append(str(diff))
    
    # Remove leading zeros
    while len(result) > 1 and result[-1] == '0':
        result.pop()
    
    result_str = ''.join(result[::-1])
    
    if result_str == '0':
        return '0'
    
    return '-' + result_str if result_negative else result_str