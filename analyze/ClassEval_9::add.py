@staticmethod
def add(num1, num2):
    """
        把两个大数字相加。
        :param num1: 要相加的第一个数字，字符串。
        :param num2: 要相加的第二个数字，字符串。
        :return: 两个数字的和，字符串。
        >>> bigNum = BigNumCalculator()
        >>> bigNum.add("12345678901234567890", "98765432109876543210")
        '111111111011111111100'

        """
    max_len = max(len(num1), len(num2))
    num1 = num1.zfill(max_len)
    num2 = num2.zfill(max_len)
    carry = 0
    result = []
    for i in range(max_len - 1, -1, -1):
        digit_sum = int(num1[i]) + int(num2[i]) + carry
        carry = digit_sum // 10
        result.insert(0, str(digit_sum % 10))
    if carry:
        result.insert(0, str(carry))
    return ''.join(result)