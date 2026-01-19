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
    # Definizione delle precedenze degli operatori
    precedence = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
        '^': 3,
        '**': 3
    }
    
    # Ottieni la precedenza degli operatori
    cur_precedence = precedence.get(cur, 0)
    peek_precedence = precedence.get(peek, 0)
    
    # Restituisce True se cur ha precedenza >= peek
    return cur_precedence >= peek_precedence