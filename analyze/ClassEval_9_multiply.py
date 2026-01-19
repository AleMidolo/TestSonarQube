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
    num1 = num1.lstrip('0')
    num2 = num2.lstrip('0')
    if not num1 or not num2:
        return '0'
    num1 = num1[::-1]
    num2 = num2[::-1]
    result = [0] * (len(num1) + len(num2))
    for i in range(len(num1)):
        for j in range(len(num2)):
            product = int(num1[i]) * int(num2[j])
            result[i + j] += product
            result[i + j + 1] += result[i + j] // 10
            result[i + j] %= 10
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    result_str = ''.join((str(digit) for digit in reversed(result)))
    if negative:
        result_str = '-' + result_str
    return result_str