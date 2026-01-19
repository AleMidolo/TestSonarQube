@staticmethod
def multiply(num1, num2):
    """
    Moltiplica due grandi numeri.
    :param num1: Il primo numero da moltiplicare, str.
    :param num2: Il secondo numero da moltiplicare, str.
    :return: Il prodotto dei due numeri, str.
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
    
    # Reverse the strings for easier manipulation (least significant digit first)
    num1 = num1[::-1]
    num2 = num2[::-1]
    
    # Initialize result array
    result = [0] * (len(num1) + len(num2))
    
    # Multiply each digit of num1 with each digit of num2
    for i in range(len(num1)):
        for j in range(len(num2)):
            digit1 = int(num1[i])
            digit2 = int(num2[j])
            product = digit1 * digit2
            
            # Add to the appropriate position
            result[i + j] += product
            
            # Handle carry
            carry = result[i + j] // 10
            result[i + j] %= 10
            
            # Propagate carry
            k = i + j + 1
            while carry > 0:
                result[k] += carry
                carry = result[k] // 10
                result[k] %= 10
                k += 1
    
    # Convert result array to string (reverse back)
    result_str = ''.join(map(str, result[::-1]))
    
    # Remove leading zeros
    result_str = result_str.lstrip('0')
    
    # Handle case where result is 0
    if not result_str:
        result_str = "0"
    
    # Add negative sign if needed
    if negative and result_str != "0":
        result_str = '-' + result_str
    
    return result_str