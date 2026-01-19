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
    
    # Convert strings to lists of digits (reversed for easier calculation)
    digits1 = [int(d) for d in num1[::-1]]
    digits2 = [int(d) for d in num2[::-1]]
    
    # Initialize result array
    result = [0] * (len(digits1) + len(digits2))
    
    # Multiply each digit of num1 with each digit of num2
    for i in range(len(digits1)):
        for j in range(len(digits2)):
            result[i + j] += digits1[i] * digits2[j]
            # Handle carry
            if result[i + j] >= 10:
                result[i + j + 1] += result[i + j] // 10
                result[i + j] %= 10
    
    # Remove leading zeros
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    
    # Convert result to string
    result_str = ''.join(str(d) for d in result[::-1])
    
    return ('-' + result_str) if negative else result_str