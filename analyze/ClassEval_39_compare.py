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
    # Definir la precedencia de los operadores
    precedence = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
        '%': 2,
        '^': 3,
        '**': 3
    }
    
    # Obtener la precedencia de cada operador
    cur_precedence = precedence.get(cur, 0)
    peek_precedence = precedence.get(peek, 0)
    
    # Retornar True si la precedencia del operador actual es mayor o igual
    return cur_precedence >= peek_precedence