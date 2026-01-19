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
    num1_len = len(num1)
    num2_len = len(num2)
    result = [0] * (num1_len + num2_len)
    for i in range(num1_len - 1, -1, -1):
        for j in range(num2_len - 1, -1, -1):
            product = int(num1[i]) * int(num2[j]) + result[i + j + 1]
            result[i + j + 1] = product % 10
            result[i + j] += product // 10
    result_str = ''.join(map(str, result)).lstrip('0')
    return result_str if result_str else '0'