from decimal import Decimal

@staticmethod
def _calculate(first_value, second_value, current_op):
    """
    Esegue il calcolo matematico basato sugli operandi e sull'operatore forniti
    :param first_value: stringa, il primo operando
    :param second_value: stringa, il secondo operando
    :param current_op: stringa, l'operatore
    :return: decimal.Decimal, il risultato calcolato
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
    elif current_op == '^':
        return num1 ** num2
    else:
        raise ValueError(f"Operatore non supportato: {current_op}")