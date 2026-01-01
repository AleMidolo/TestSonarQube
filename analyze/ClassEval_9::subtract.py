@staticmethod
def subtract(num1, num2):
    """
        दो बड़े नंबरों को घटाता है।
        :param num1: घटाने के लिए पहला नंबर, str.
        :param num2: घटाने के लिए दूसरा नंबर, str.
        :return: दोनों नंबरों का अंतर, str.
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
    max_length = max(len(num1), len(num2))
    num1 = num1.zfill(max_length)
    num2 = num2.zfill(max_length)
    result = []
    borrow = 0
    for i in range(max_length - 1, -1, -1):
        sub = int(num1[i]) - int(num2[i]) - borrow
        if sub < 0:
            sub += 10
            borrow = 1
        else:
            borrow = 0
        result.insert(0, str(sub))
    while len(result) > 1 and result[0] == '0':
        result.pop(0)
    return ('-' if negative else '') + ''.join(result)