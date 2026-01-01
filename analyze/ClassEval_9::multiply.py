@staticmethod
def multiply(num1, num2):
    """
        Multiplies two big numbers.
        :param num1: The first number to multiply,str.
        :param num2: The second number to multiply,str.
        :return: The product of the two numbers,str.
        >>> bigNum = BigNumCalculator()
        >>> bigNum.multiply("12345678901234567890", "98765432109876543210")
        '1219326311370217952237463801111263526900'
        """
    if num1 == '0' or num2 == '0':
        return '0'
    result = '0'
    num1_len = len(num1)
    num2_len = len(num2)
    for i in range(num2_len):
        current_digit = int(num2[num2_len - 1 - i])
        current_product = BigNumCalculator.add(num1 + '0' * i, '0' * (current_digit * int(num1)))
        result = BigNumCalculator.add(result, current_product)
    return result