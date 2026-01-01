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
    cur_index = self.get_operat_priority(cur)
    peek_index = self.get_operat_priority(peek)
    return self.operat_priority[cur_index] >= self.operat_priority[peek_index]