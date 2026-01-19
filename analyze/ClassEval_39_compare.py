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
    cur_priority = self.get_priority(cur)
    peek_priority = self.get_priority(peek)
    return cur_priority >= peek_priority