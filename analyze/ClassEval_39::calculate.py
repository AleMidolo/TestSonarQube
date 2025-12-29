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
    calc_stack = deque()
    for token in self.postfix_stack:
        if self.is_operator(token):
            if token == '~':
                if not calc_stack:
                    raise ValueError('Invalid expression: missing operand for unary minus')
                operand = calc_stack.pop()
                result = Decimal(0) - Decimal(operand)
                calc_stack.append(str(result))
            else:
                if len(calc_stack) < 2:
                    raise ValueError('Invalid expression: insufficient operands for operator {}'.format(token))
                second_value = calc_stack.pop()
                first_value = calc_stack.pop()
                result = self._calculate(first_value, second_value, token)
                calc_stack.append(str(result))
        else:
            calc_stack.append(token)
    if len(calc_stack) != 1:
        raise ValueError('Invalid expression: could not compute final result')
    result = Decimal(calc_stack.pop())
    return float(result)