def calculate(self, expression):
        """
        计算给定后缀表达式的结果
        :param expression: 字符串，要计算的后缀表达式
        :return: 浮点数，计算结果
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.calculate("2 + 3 * 4")
        14.0

        """
        self.prepare(expression)
        stack = deque()

        for token in self.postfix_stack:
            if not self.is_operator(token):
                stack.append(token)
            else:
                second_value = stack.pop()
                first_value = stack.pop()
                result = self._calculate(first_value, second_value, token)
                stack.append(result)

        return float(stack.pop())