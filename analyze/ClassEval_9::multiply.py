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
    result = '0'
    num2_len = len(num2)
    for i in range(num2_len):
        digit = int(num2[num2_len - 1 - i])
        if digit != 0:
            partial_product = BigNumCalculator.add(num1 + '0' * i, '0' * (len(num1) + i - 1))
            result = BigNumCalculator.add(result, partial_product)
    return result