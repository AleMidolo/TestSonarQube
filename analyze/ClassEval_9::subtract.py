@staticmethod
def subtract(num1, num2):
    """
        Sottrae due grandi numeri.
        :param num1: Il primo numero da sottrarre, str.
        :param num2: Il secondo numero da sottrarre, str.
        :return: La differenza dei due numeri, str.
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
    num1 = list(num1)
    num2 = list(num2.zfill(len(num1)))
    result = []
    borrow = 0
    for i in range(len(num1) - 1, -1, -1):
        sub = int(num1[i]) - int(num2[i]) - borrow
        if sub < 0:
            sub += 10
            borrow = 1
        else:
            borrow = 0
        result.append(str(sub))
    result = ''.join(result[::-1]).lstrip('0')
    if negative:
        result = '-' + result
    return result if result else '0'