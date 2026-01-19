@staticmethod
def multiply(num1, num2):
    """
    Multiplica dos números grandes.
    :param num1: El primer número a multiplicar, str.
    :param num2: El segundo número a multiplicar, str.
    :return: El producto de los dos números, str.
    >>> bigNum = BigNumCalculator()
    >>> bigNum.multiply("12345678901234567890", "98765432109876543210")
    '1219326311370217952237463801111263526900'

    """
    # Handle signs
    negative = False
    if num1.startswith('-'):
        negative = not negative
        num1 = num1[1:]
    if num2.startswith('-'):
        negative = not negative
        num2 = num2[1:]
    
    # Handle zero cases
    if num1 == '0' or num2 == '0':
        return '0'
    
    # Initialize result array
    len1, len2 = len(num1), len(num2)
    result = [0] * (len1 + len2)
    
    # Reverse the strings for easier processing
    num1 = num1[::-1]
    num2 = num2[::-1]
    
    # Multiply each digit
    for i in range(len1):
        for j in range(len2):
            digit1 = int(num1[i])
            digit2 = int(num2[j])
            result[i + j] += digit1 * digit2
            
            # Handle carry
            result[i + j + 1] += result[i + j] // 10
            result[i + j] %= 10
    
    # Convert result array to string
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    
    result_str = ''.join(map(str, result[::-1]))
    
    return ('-' + result_str) if negative else result_str