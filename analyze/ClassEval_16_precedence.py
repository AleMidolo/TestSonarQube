def precedence(self, operator):
    """
    Devuelve la prioridad del operador especificado, donde cuanto mayor es la prioridad, mayor es la asignación. La prioridad de '^' es mayor que la de '/' y '*', y la prioridad de '/' y '*' es mayor que la de '+' y '-'
    :param operator: cadena, operador dado
    :return: int, la prioridad del operador dado, de lo contrario devuelve 0
    >>> calculator = Calculator()
    >>> calculator.precedence('+')
    1
    >>> calculator.precedence('^')
    3
    """
    if operator in ['+', '-']:
        return 1
    elif operator in ['*', '/']:
        return 2
    elif operator == '^':
        return 3
    else:
        return 0