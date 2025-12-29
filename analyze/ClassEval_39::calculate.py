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
    calc_stack = deque(self.postfix_stack.copy())
    result_stack = deque()
    while calc_stack:
        token = calc_stack.popleft()
        if self.is_operator(token):
            if token in {'+', '-', '*', '\\/', '%'}:
                if len(result_stack) < 2:
                    raise ValueError('Invalid expression: insufficient operands for operator {}'.format(token))
                second_value = result_stack.pop()
                first_value = result_stack.pop()
                if token == '-' and first_value == '~':
                    result = -Decimal(second_value)
                    result_stack.append(str(result))
                else:
                    result = self._calculate(first_value, second_value, token)
                    result_stack.append(str(result))
            elif token == '~':
                if len(result_stack) < 1:
                    raise ValueError('Invalid expression: insufficient operand for unary minus')
                value = result_stack.pop()
                result = -Decimal(value)
                result_stack.append(str(result))
            else:
                raise ValueError('Unexpected operator in postfix expression: {}'.format(token))
        else:
            result_stack.append(token)
    if len(result_stack) != 1:
        raise ValueError('Invalid expression: too many operands remaining')
    return float(Decimal(result_stack.pop()))