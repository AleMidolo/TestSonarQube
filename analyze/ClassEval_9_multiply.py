@staticmethod
def multiply(num1, num2):
    """
    दो बड़े संख्याओं को गुणा करता है।
    :param num1: गुणा करने के लिए पहला संख्या, str.
    :param num2: गुणा करने के लिए दूसरा संख्या, str.
    :return: दोनों संख्याओं का गुणनफल, str.
    >>> bigNum = BigNumCalculator()
    >>> bigNum.multiply("12345678901234567890", "98765432109876543210")
    '1219326311370217952237463801111263526900'

    """
    # Handle edge cases
    if num1 == "0" or num2 == "0":
        return "0"
    
    # Determine sign of result
    negative = False
    if num1[0] == '-':
        negative = not negative
        num1 = num1[1:]
    if num2[0] == '-':
        negative = not negative
        num2 = num2[1:]
    
    # Reverse the strings for easier processing (least significant digit first)
    num1 = num1[::-1]
    num2 = num2[::-1]
    
    # Initialize result array
    result = [0] * (len(num1) + len(num2))
    
    # Multiply each digit of num1 with each digit of num2
    for i in range(len(num1)):
        for j in range(len(num2)):
            digit1 = int(num1[i])
            digit2 = int(num2[j])
            
            # Multiply and add to the appropriate position
            result[i + j] += digit1 * digit2
            
            # Handle carry
            if result[i + j] >= 10:
                result[i + j + 1] += result[i + j] // 10
                result[i + j] %= 10
    
    # Convert result array to string
    # Remove leading zeros
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    
    # Reverse to get the correct order
    result_str = ''.join(map(str, result[::-1]))
    
    # Add negative sign if needed
    if negative:
        result_str = '-' + result_str
    
    return result_str