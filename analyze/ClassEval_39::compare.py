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
    return self.operat_priority[{'(': 0, '+': 1, '-': 1, '*': 2, '\\/': 2, '%': 2}.get(cur, -1)] >= self.operat_priority[{'(': 0, '+': 1, '-': 1, '*': 2, '\\/': 2, '%': 2}.get(peek, -1)]