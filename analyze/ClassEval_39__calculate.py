@staticmethod
def _calculate(first_value, second_value, current_op):
    """
    Perform the mathematical calculation based on the given operands and operator
    :param first_value: string, the first operand
    :param second_value: string, the second operand
    :param current_op: string, the operator
    :return: decimal.Decimal, the calculated result
    >>> expression_calculator = ExpressionCalculator()
    >>> expression_calculator._calculate("2", "3", "+")
    5.0

    """
    from decimal import Decimal
    
    first = Decimal(first_value)
    second = Decimal(second_value)
    
    if current_op == '+':
        return first + second
    elif current_op == '-':
        return first - second
    elif current_op == '*':
        return first * second
    elif current_op == '/':
        return first / second
    elif current_op == '//':
        return first // second
    elif current_op == '%':
        return first % second
    elif current_op == '**':
        return first ** second
    else:
        raise ValueError(f"Unsupported operator: {current_op}")