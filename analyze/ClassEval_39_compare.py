def compare(self, cur, peek):
    """
    Confronta la precedenza di due operatori
    :param cur: stringa, l'operatore corrente
    :param peek: stringa, l'operatore in cima allo stack degli operatori
    :return: bool, True se l'operatore corrente ha una precedenza maggiore o uguale, False altrimenti
    >>> expression_calculator = ExpressionCalculator()
    >>> expression_calculator.compare("+", "-")
    True

    """
    return self.operat_priority[self.get_operator_index(cur)] >= self.operat_priority[self.get_operator_index(peek)]