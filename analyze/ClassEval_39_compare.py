def compare(self, cur, peek):
    """
    比较两个运算符的优先级
    :param cur: 字符串，当前运算符
    :param peek: 字符串，运算符栈顶部的运算符
    :return: 布尔值，如果当前运算符具有更高或相等的优先级，则为 True，否则为 False
    >>> expression_calculator = ExpressionCalculator()
    >>> expression_calculator.compare("+", "-")
    True

    """
    # 定义运算符优先级
    precedence = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
        '%': 2,
        '^': 3,
        '**': 3,
        '(': 0
    }
    
    # 获取当前运算符和栈顶运算符的优先级
    cur_precedence = precedence.get(cur, 0)
    peek_precedence = precedence.get(peek, 0)
    
    # 如果当前运算符优先级大于或等于栈顶运算符优先级，返回 True
    return cur_precedence >= peek_precedence