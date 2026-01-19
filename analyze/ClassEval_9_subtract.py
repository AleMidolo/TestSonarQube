@staticmethod
def subtract(num1, num2):
    """
    दो बड़े नंबरों को घटाता है।
    :param num1: घटाने के लिए पहला नंबर, str.
    :param num2: घटाने के लिए दूसरा नंबर, str.
    :return: दोनों नंबरों का अंतर, str.
    >>> bigNum = BigNumCalculator()
    >>> bigNum.subtract("12345678901234567890", "98765432109876543210")
    '-86419753208641975320'

    """
    # Handle signs
    if num1.startswith('-') and num2.startswith('-'):
        # -a - (-b) = b - a
        return BigNumCalculator.subtract(num2[1:], num1[1:])
    elif num1.startswith('-'):
        # -a - b = -(a + b)
        return '-' + BigNumCalculator.add(num1[1:], num2)
    elif num2.startswith('-'):
        # a - (-b) = a + b
        return BigNumCalculator.add(num1, num2[1:])
    
    # Both numbers are positive
    # Determine which is larger
    is_negative = False
    if len(num1) < len(num2) or (len(num1) == len(num2) and num1 < num2):
        # num1 < num2, so result will be negative
        num1, num2 = num2, num1
        is_negative = True
    
    # Perform subtraction
    result = []
    borrow = 0
    
    # Pad num2 with leading zeros
    num2 = num2.zfill(len(num1))
    
    # Subtract from right to left
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
    
    # Handle case where result is 0
    if not result_str:
        result_str = '0'
    
    # Add negative sign if needed
    if is_negative and result_str != '0':
        result_str = '-' + result_str
    
    return result_str