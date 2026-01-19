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
    negative = False
    if len(num1) < len(num2):
        negative = True
    elif len(num1) == len(num2):
        for i in range(len(num1)):
            if int(num1[i]) < int(num2[i]):
                negative = True
                break
            elif int(num1[i]) > int(num2[i]):
                break
    if negative:
        num1, num2 = (num2, num1)
    max_length = max(len(num1), len(num2))
    num1 = num1.zfill(max_length)
    num2 = num2.zfill(max_length)
    borrow = 0
    result = []
    for i in range(max_length - 1, -1, -1):
        digit1 = int(num1[i])
        digit2 = int(num2[i])
        digit1 -= borrow
        if digit1 < digit2:
            digit1 += 10
            borrow = 1
        else:
            borrow = 0
        diff = digit1 - digit2
        result.insert(0, str(diff))
    while len(result) > 1 and result[0] == '0':
        result.pop(0)
    if negative:
        result.insert(0, '-')
    return ''.join(result)