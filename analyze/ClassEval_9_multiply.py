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
    if num1 == '0' or num2 == '0':
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
    return ''.join(map(str, result[::-1]))