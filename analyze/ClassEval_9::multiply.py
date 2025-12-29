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
    negative = False
    if num1[0] == '-':
        negative = not negative
        num1 = num1[1:]
    if num2[0] == '-':
        negative = not negative
        num2 = num2[1:]
    num1 = num1.lstrip('0') or '0'
    num2 = num2.lstrip('0') or '0'
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
    result_str = ''.join(map(str, result)).lstrip('0')
    if not result_str:
        result_str = '0'
    if negative and result_str != '0':
        result_str = '-' + result_str
    return result_str