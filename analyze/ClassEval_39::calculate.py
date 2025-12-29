def calculate(self, expression):
    """
        Calculate the result of the given postfix expression
        :param expression: string, the postfix expression to be calculated
        :return: float, the calculated result
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.calculate("2 + 3 * 4")
        14.0

        """
    transformed_expression = self.transform(expression)
    self.postfix_stack.clear()
    self.prepare(transformed_expression)
    calc_stack = deque(self.postfix_stack.copy())
    result_stack = deque()
    while calc_stack:
        token = calc_stack.popleft()
        if self.is_operator(token):
            if len(result_stack) < 2:
                raise ValueError('Invalid expression: insufficient operands')
            second_value = result_stack.pop()
            first_value = result_stack.pop()
            if token == '~':
                result_stack.append(first_value)
                result = -Decimal(second_value)
                result_stack.append(str(result))
            else:
                result = self._calculate(first_value, second_value, token)
                result_stack.append(str(result))
        else:
            result_stack.append(token)
    if len(result_stack) != 1:
        raise ValueError('Invalid expression: too many values in result stack')
    return float(Decimal(result_stack.pop()))