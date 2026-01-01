@staticmethod
def _calculate(first_value, second_value, current_op):
    """
        Realiza el cálculo matemático basado en los operandos y el operador dados
        :param first_value: string, el primer operando
        :param second_value: string, el segundo operando
        :param current_op: string, el operador
        :return: decimal.Decimal, el resultado calculado
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator._calculate("2", "3", "+")
        5.0
        """
    first_value = Decimal(first_value)
    second_value = Decimal(second_value)
    if current_op == '+':
        return first_value + second_value
    elif current_op == '-':
        return first_value - second_value
    elif current_op == '*':
        return first_value * second_value
    elif current_op == '\\/':
        return first_value / second_value
    elif current_op == '%':
        return first_value % second_value