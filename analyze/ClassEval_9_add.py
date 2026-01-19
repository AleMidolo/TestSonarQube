@staticmethod
def add(num1, num2):
    """
        Suma dos números grandes.
        :param num1: El primer número a sumar, str.
        :param num2: El segundo número a sumar, str.
        :return: La suma de los dos números, str.
        >>> bigNum = BigNumCalculator()
        >>> bigNum.add("12345678901234567890", "98765432109876543210")
        '111111111011111111100'
        """
    len1, len2 = (len(num1), len(num2))
    max_length = max(len1, len2)
    num1 = num1.zfill(max_length)
    num2 = num2.zfill(max_length)
    carry = 0
    result = []
    for i in range(max_length - 1, -1, -1):
        total = int(num1[i]) + int(num2[i]) + carry
        result.append(str(total % 10))
        carry = total // 10
    if carry:
        result.append(str(carry))
    return ''.join(result[::-1])