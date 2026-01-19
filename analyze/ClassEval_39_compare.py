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
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    
    # Get precedence values, default to 0 if operator not found
    cur_precedence = precedence.get(cur, 0)
    peek_precedence = precedence.get(peek, 0)
    
    # Return True if current operator has higher or equal precedence
    return cur_precedence >= peek_precedence