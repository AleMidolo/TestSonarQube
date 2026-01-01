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
    result = []
    borrow = 0
    for i in range(len(num1)):
        digit1 = int(num1[i])
        digit2 = int(num2[i]) if i < len(num2) else 0
        if digit1 < digit2 + borrow:
            digit1 += 10
            borrow = 1
        else:
            borrow = 0
        result.append(str(digit1 - digit2 - borrow))
    while result and result[-1] == '0':
        result.pop()
    if negative:
        result.append('-')
    return ''.join(result[::-1]) if result else '0'