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
    calc_stack = deque(self.postfix_stack)
    result_stack = deque()
    while calc_stack:
        token = calc_stack.popleft()
        if self.is_operator(token):
            if token == '~':
                if not result_stack:
                    raise ValueError('Invalid expression: missing operand for unary minus')
                operand = result_stack.pop()
                result_stack.append(-Decimal(operand))
            else:
                if len(result_stack) < 2:
                    raise ValueError('Invalid expression: insufficient operands for operator {}'.format(token))
                second_value = result_stack.pop()
                first_value = result_stack.pop()
                result = self._calculate(first_value, second_value, token)
                result_stack.append(result)
        else:
            result_stack.append(token)
    if len(result_stack) != 1:
        raise ValueError('Invalid expression: too many operands or operators')
    return float(result_stack.pop())