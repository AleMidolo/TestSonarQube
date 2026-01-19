@staticmethod
def multiply(num1, num2):
    """
        दो बड़े संख्याओं को गुणा करता है।
        :param num1: गुणा करने के लिए पहला संख्या, str.
        :param num2: गुणा करने के लिए दूसरा संख्या, str.
        :return: दोनों संख्याओं का गुणनफल, str.
        >>> bigNum = BigNumCalculator()
        >>> bigNum.multiply("12345678901234567890", "98765432109876543210")
        '1219326311370217952237463801111263526900'
        """
    if num1 == '0' or num2 == '0':
        return '0'
    len1, len2 = (len(num1), len(num2))
    result = [0] * (len1 + len2)
    for i in range(len1 - 1, -1, -1):
        for j in range(len2 - 1, -1, -1):
            product = int(num1[i]) * int(num2[j]) + result[i + j + 1]
            result[i + j + 1] = product % 10
            result[i + j] += product // 10
    result_str = ''.join(map(str, result)).lstrip('0')
    return result_str if result_str else '0'