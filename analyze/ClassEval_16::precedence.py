def precedence(self, operator):
    """
        Restituisce la priorità dell'operatore specificato, dove maggiore è la priorità, maggiore è l'assegnazione. La priorità di '^' è maggiore di '/' e '*', e la priorità di '/' e '*' è maggiore di '+' e '-'
        :param operator: stringa, operatore fornito
        :return: int, la priorità dell'operatore fornito, altrimenti restituisce 0
        >>> calculator = Calculator()
        >>> calculator.precedence('+')
        1
        >>> calculator.precedence('^')
        3
        """
    if operator == '^':
        return 3
    elif operator in '*/':
        return 2
    elif operator in '+-':
        return 1
    return 0