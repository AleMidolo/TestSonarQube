from decimal import Decimal

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
    num1 = Decimal(first_value)
    num2 = Decimal(second_value)
    
    if current_op == '+':
        return num1 + num2
    elif current_op == '-':
        return num1 - num2
    elif current_op == '*':
        return num1 * num2
    elif current_op == '/':
        return num1 / num2
    elif current_op == '^' or current_op == '**':
        return num1 ** num2
    else:
        raise ValueError(f"Operador no soportado: {current_op}")