@staticmethod
def add(num1, num2):
    """
        Aggiunge due grandi numeri.
        :param num1: Il primo numero da aggiungere, str.
        :param num2: Il secondo numero da aggiungere, str.
        :return: La somma dei due numeri, str.
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