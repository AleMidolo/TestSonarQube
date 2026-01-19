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