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
    if num1 == '0' or num2 == '0':
        return '0'
    negative = False
    if num1[0] == '-':
        negative = not negative
        num1 = num1[1:]
    if num2[0] == '-':
        negative = not negative
        num2 = num2[1:]
    num1 = num1.lstrip('0') or '0'
    num2 = num2.lstrip('0') or '0'
    num1 = num1[::-1]
    num2 = num2[::-1]
    result = [0] * (len(num1) + len(num2))
    for i in range(len(num1)):
        digit1 = int(num1[i])
        carry = 0
        for j in range(len(num2)):
            digit2 = int(num2[j])
            product = digit1 * digit2 + result[i + j] + carry
            result[i + j] = product % 10
            carry = product // 10
        if carry > 0:
            result[i + len(num2)] += carry
    result_str = ''.join((str(digit) for digit in result[::-1]))
    result_str = result_str.lstrip('0') or '0'
    if negative and result_str != '0':
        result_str = '-' + result_str
    return result_str