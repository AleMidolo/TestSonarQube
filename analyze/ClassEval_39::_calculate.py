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
    if current_op == '+':
        return Decimal(first_value) + Decimal(second_value)
    elif current_op == '-':
        return Decimal(first_value) - Decimal(second_value)
    elif current_op == '*':
        return Decimal(first_value) * Decimal(second_value)
    elif current_op == '\\/':
        return Decimal(first_value) / Decimal(second_value)
    elif current_op == '%':
        return Decimal(first_value) % Decimal(second_value)