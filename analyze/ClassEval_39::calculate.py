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
    transformed_expr = self.transform(expression)
    self.prepare(transformed_expr)
    result_stack = deque()
    for token in self.postfix_stack:
        if self.is_operator(token):
            if token == '~':
                if result_stack:
                    operand = result_stack.pop()
                    result_stack.append(-Decimal(operand))
            else:
                if len(result_stack) < 2:
                    raise ValueError('Invalid expression: insufficient operands')
                second = result_stack.pop()
                first = result_stack.pop()
                result = self._calculate(first, second, token)
                result_stack.append(result)
        else:
            result_stack.append(token)
    if not result_stack:
        raise ValueError('Invalid expression: no result')
    result = float(result_stack.pop())
    self.postfix_stack.clear()
    return result