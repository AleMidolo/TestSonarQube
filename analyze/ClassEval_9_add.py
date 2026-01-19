@staticmethod
def add(num1, num2):
    """
        दो बड़े नंबर जोड़ता है।
        :param num1: जोड़ने के लिए पहला नंबर, str.
        :param num2: जोड़ने के लिए दूसरा नंबर, str.
        :return: दोनों नंबरों का योग, str.
        >>> bigNum = BigNumCalculator()
        >>> bigNum.add("12345678901234567890", "98765432109876543210")
        '111111111011111111100'

        """
    max_length = max(len(num1), len(num2))
    num1 = num1.zfill(max_length)
    num2 = num2.zfill(max_length)
    carry = 0
    result = []
    for i in range(max_length - 1, -1, -1):
        digit_sum = int(num1[i]) + int(num2[i]) + carry
        carry = digit_sum // 10
        result.insert(0, str(digit_sum % 10))
    if carry:
        result.insert(0, str(carry))
    return ''.join(result)