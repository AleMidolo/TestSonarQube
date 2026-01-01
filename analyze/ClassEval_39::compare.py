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
        return self.operat_priority[self.get_operator_index(cur)] >= self.operat_priority[self.get_operator_index(peek)]

    def get_operator_index(self, operator):
        """
        获取运算符的优先级索引
        :param operator: 字符串，运算符
        :return: int, 运算符的优先级索引
        """
        operators = {'+': 0, '-': 1, '*': 2, '\/': 3, '%': 4, '(': 5, ')': 6}
        return operators.get(operator, -1)