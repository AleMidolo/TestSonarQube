from decimal import Decimal

@staticmethod
def _calculate(first_value, second_value, current_op):
    """
    दिए गए ऑपरेटर और ऑपरेनड के आधार पर गणितीय गणना करें
    :param first_value: string, पहला ऑपरेनड
    :param second_value: string, दूसरा ऑपरेनड
    :param current_op: string, ऑपरेटर
    :return: decimal.Decimal, गणना किया गया परिणाम
    >>> expression_calculator = ExpressionCalculator()
    >>> expression_calculator._calculate("2", "3", "+")
    5.0

    """
    num1 = Decimal(first_value)
    num2 = Decimal(second_value)
    
    if current_op == '+':
        return float(num1 + num2)
    elif current_op == '-':
        return float(num1 - num2)
    elif current_op == '*':
        return float(num1 * num2)
    elif current_op == '/':
        return float(num1 / num2)
    elif current_op == '//':
        return float(num1 // num2)
    elif current_op == '%':
        return float(num1 % num2)
    elif current_op == '**':
        return float(num1 ** num2)
    else:
        raise ValueError(f"Unsupported operator: {current_op}")