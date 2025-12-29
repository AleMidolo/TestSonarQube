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
        return self.operat_priority[self.get_operator_index(cur)] >= self.operat_priority[self.get_operator_index(peek)]

    @staticmethod
    def get_operator_index(op):
        """
        Get the index of the operator in the operator priority list
        :param op: string, the operator
        :return: int, the index of the operator
        """
        operators = {'+': 0, '-': 1, '*': 2, '\/': 3, '%': 4, '(': 5, ')': 6}
        return operators.get(op, -1)