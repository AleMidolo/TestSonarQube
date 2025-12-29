def precedence(self, operator):
    """
        返回指定运算符的优先级，优先级越高，赋值越大。'^' 的优先级高于 '/' 和 '*'，而 '/' 和 '*' 的优先级高于 '+' 和 '-'
        :param operator: 字符串，给定的运算符
        :return: int，给定运算符的优先级，否则返回 0
        >>> calculator = Calculator()
        >>> calculator.precedence('+')
        1
        >>> calculator.precedence('^')
        3
        """
    if operator == '^':
        return 3
    elif operator in ['*', '/']:
        return 2
    elif operator in ['+', '-']:
        return 1
    else:
        return 0