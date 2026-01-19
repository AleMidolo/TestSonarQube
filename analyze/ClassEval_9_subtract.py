@staticmethod
def subtract(num1, num2):
    """
        Resta dos números grandes.
        :param num1: El primer número a restar, str.
        :param num2: El segundo número a restar, str.
        :return: La diferencia de los dos números, str.
        >>> bigNum = BigNumCalculator()
        >>> bigNum.subtract("12345678901234567890", "98765432109876543210")
        '-86419753208641975320'
        """
    if num1 == num2:
        return '0'
    negative = False
    if num1 < num2:
        num1, num2 = (num2, num1)
        negative = True
    num1 = num1[::-1]
    num2 = num2[::-1]
    max_length = max(len(num1), len(num2))
    num2 += '0' * (max_length - len(num2))
    result = []
    borrow = 0
    for i in range(max_length):
        digit1 = int(num1[i])
        digit2 = int(num2[i]) + borrow
        if digit1 < digit2:
            digit1 += 10
            borrow = 1
        else:
            borrow = 0
        result.append(str(digit1 - digit2))
    while result and result[-1] == '0':
        result.pop()
    if negative:
        result.append('-')
    return ''.join(result[::-1]) if result else '0'