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
    num1 = num1[::-1]
    num2 = num2[::-1]
    result = []
    borrow = 0
    for i in range(len(num1)):
        digit1 = int(num1[i])
        digit2 = int(num2[i]) if i < len(num2) else 0
        if digit1 < digit2 + borrow:
            digit1 += 10
            result.append(str(digit1 - digit2 - borrow))
            borrow = 1
        else:
            result.append(str(digit1 - digit2 - borrow))
            borrow = 0
    result = ''.join(result[::-1]).lstrip('0')
    return '-' + result if negative else result