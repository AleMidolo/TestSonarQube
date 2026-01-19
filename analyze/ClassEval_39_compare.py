def compare(self, cur, peek):
    """
    Compare the precedence of two operators
    :param cur: string, the current operator
    :param peek: string, the operator at the top of the operator stack
    :return: bool, True if the current operator has higher or equal precedence, False otherwise
    >>> expression_calculator = ExpressionCalculator()
    >>> expression_calculator.compare("+", "-")
    True

    """
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    return precedence.get(cur, 0) >= precedence.get(peek, 0)