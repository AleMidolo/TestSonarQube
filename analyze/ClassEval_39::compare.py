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

def get_operator_index(self, operator):
    """
    Restituisce l'indice dell'operatore nella lista delle priorità
    :param operator: stringa, l'operatore di cui si desidera ottenere l'indice
    :return: int, l'indice dell'operatore
    """
    operators = ['+', '-', '*', '\/', '(', ')', '%']
    return operators.index(operator) if operator in operators else -1