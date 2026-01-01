def calculate(self, expression):
    """
        计算给定后缀表达式的结果
        :param expression: 字符串，要计算的后缀表达式
        :return: 浮点数，计算结果
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.calculate("2 + 3 * 4")
        14.0

        """
    self.postfix_stack.clear()
    expression = self.transform(expression)
    self.prepare(expression)
    op_stack = deque()
    for token in self.postfix_stack:
        if not self.is_operator(token):
            op_stack.append(token)
        else:
            second_value = op_stack.pop()
            first_value = op_stack.pop()
            result = self._calculate(first_value, second_value, token)
            op_stack.append(str(result))
    return float(op_stack.pop())