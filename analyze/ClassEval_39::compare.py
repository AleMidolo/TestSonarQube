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
    index1 = self.get_priority_index(cur)
    index2 = self.get_priority_index(peek)
    return self.operat_priority[index1] <= self.operat_priority[index2] and self.operat_priority[index1] != -1