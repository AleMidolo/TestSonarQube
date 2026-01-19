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
    
    # Both positive numbers
    # Determine which is larger
    if len(num1) > len(num2):
        is_negative = False
    elif len(num2) > len(num1):
        is_negative = True
    else:
        if num1 >= num2:
            is_negative = False
        else:
            is_negative = True
    
    # If result will be negative, swap and add negative sign
    if is_negative:
        num1, num2 = num2, num1
    
    # Pad the shorter number with zeros
    max_len = max(len(num1), len(num2))
    num1 = num1.zfill(max_len)
    num2 = num2.zfill(max_len)
    
    # Perform subtraction from right to left
    result = []
    borrow = 0
    
    for i in range(max_len - 1, -1, -1):
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
    result = ''.join(reversed(result)).lstrip('0')
    
    # Handle zero case
    if not result:
        result = '0'
    
    # Add negative sign if needed
    if is_negative:
        result = '-' + result
    
    return result