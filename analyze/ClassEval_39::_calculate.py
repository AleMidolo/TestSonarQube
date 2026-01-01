@staticmethod
def _calculate(first_value, second_value, current_op):
    """
        Perform mathematical calculation based on given operator and operands
        :param first_value: string, first operand
        :param second_value: string, second operand
        :param current_op: string, operator
        :return: decimal.Decimal, calculated result
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator._calculate("2", "3", "+")
        5.0
        """
    first = Decimal(first_value)
    second = Decimal(second_value)
    if current_op == '+':
        return first + second
    elif current_op == '-':
        return first - second
    elif current_op == '*':
        return first * second
    elif current_op == '/':
        if second == 0:
            raise ZeroDivisionError('Division by zero')
        return first / second
    elif current_op == '%':
        if second == 0:
            raise ZeroDivisionError('Modulo by zero')
        return first % second
    else:
        raise ValueError(f'Unsupported operator: {current_op}')