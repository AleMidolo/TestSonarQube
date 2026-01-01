def compare(self, cur, peek):
    """
        Compare the priority of two operators
        :param cur: string, current operator
        :param peek: string, operator at the top of the operator stack
        :return: bool, True if current operator has higher or equal priority, False otherwise
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.compare("+", "-")
        True
        """
    cur_index = self._get_operator_index(cur)
    peek_index = self._get_operator_index(peek)
    return self.operat_priority[cur_index] <= self.operat_priority[peek_index]