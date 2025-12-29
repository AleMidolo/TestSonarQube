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
    transformed_expression = self.transform(expression)
    self.prepare(transformed_expression)
    result_stack = deque()
    for item in self.postfix_stack:
        if self.is_operator(item):
            if item == '~':
                if result_stack:
                    operand = result_stack.pop()
                    result_stack.append(Decimal(0) - Decimal(operand))
            elif len(result_stack) >= 2:
                second = result_stack.pop()
                first = result_stack.pop()
                result = self._calculate(first, second, item)
                result_stack.append(result)
        else:
            result_stack.append(item)
    if result_stack:
        result = float(result_stack.pop())
        return result
    else:
        return 0.0