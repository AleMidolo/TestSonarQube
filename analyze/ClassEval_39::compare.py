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
    cur_index = self.get_index(cur)
    peek_index = self.get_index(peek)
    return self.operat_priority[cur_index] >= self.operat_priority[peek_index]