def calculate(self, expression):
    """
        Calculate the result of the given postfix expression
        :param expression: string, the postfix expression to be calculated
        :return: float, the calculated result
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.calculate("2 + 3 * 4")
        14.0

        """
    self.postfix_stack.clear()
    transformed_expression = self.transform(expression)
    self.prepare(transformed_expression)
    calc_stack = deque(self.postfix_stack.copy())
    result_stack = deque()
    while calc_stack:
        token = calc_stack.popleft()
        if self.is_operator(token):
            if token == '~':
                if result_stack:
                    operand = result_stack.pop()
                    result_stack.append(str(-Decimal(operand)))
            else:
                if len(result_stack) < 2:
                    raise ValueError('Invalid expression: insufficient operands')
                second_value = result_stack.pop()
                first_value = result_stack.pop()
                if first_value.startswith('~'):
                    first_value = '-' + first_value[1:]
                if second_value.startswith('~'):
                    second_value = '-' + second_value[1:]
                result = self._calculate(first_value, second_value, token)
                result_stack.append(str(result))
        else:
            if token.startswith('~'):
                token = '-' + token[1:]
            result_stack.append(token)
    if len(result_stack) != 1:
        raise ValueError('Invalid expression: could not compute final result')
    result = Decimal(result_stack.pop())
    return float(result)