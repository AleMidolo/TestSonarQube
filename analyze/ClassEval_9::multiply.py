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
    len1, len2 = (len(num1), len(num2))
    result = [0] * (len1 + len2)
    for i in range(len1 - 1, -1, -1):
        carry = 0
        n1 = int(num1[i])
        for j in range(len2 - 1, -1, -1):
            n2 = int(num2[j])
            temp_sum = n1 * n2 + result[i + j + 1] + carry
            carry = temp_sum // 10
            result[i + j + 1] = temp_sum % 10
        result[i] += carry
    start = 0
    while start < len(result) and result[start] == 0:
        start += 1
    if start == len(result):
        return '0'
    return ''.join((str(x) for x in result[start:]))