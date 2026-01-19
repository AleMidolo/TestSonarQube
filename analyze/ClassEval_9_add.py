@staticmethod
def add(num1, num2):
    """
        Suma dos números grandes.
        :param num1: El primer número a sumar, str.
        :param num2: El segundo número a sumar, str.
        :return: La suma de los dos números, str.
        >>> bigNum = BigNumCalculator()
        >>> bigNum.add("12345678901234567890", "98765432109876543210")
        '111111111011111111100'

        """
    num1_negative = num1.startswith('-')
    num2_negative = num2.startswith('-')
    if not num1_negative and (not num2_negative):
        return BigNumCalculator._add_positive(num1, num2)
    elif num1_negative and num2_negative:
        return '-' + BigNumCalculator._add_positive(num1[1:], num2[1:])
    elif num1_negative and (not num2_negative):
        return BigNumCalculator.subtract(num2, num1[1:])
    else:
        return BigNumCalculator.subtract(num1, num2[1:])