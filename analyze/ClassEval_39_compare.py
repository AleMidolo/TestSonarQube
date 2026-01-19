def compare(self, cur, peek):
    """
    Comparar la precedencia de dos operadores
    :param cur: cadena, el operador actual
    :param peek: cadena, el operador en la parte superior de la pila de operadores
    :return: bool, True si el operador actual tiene una precedencia mayor o igual, False en caso contrario
    >>> expression_calculator = ExpressionCalculator()
    >>> expression_calculator.compare("+", "-")
    True

    """
    # Define operator precedence levels
    precedence = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
        '%': 2,
        '^': 3,
        '**': 3
    }
    
    # Get precedence values, default to 0 if operator not found
    cur_precedence = precedence.get(cur, 0)
    peek_precedence = precedence.get(peek, 0)
    
    # Return True if current operator has greater or equal precedence
    return cur_precedence >= peek_precedence