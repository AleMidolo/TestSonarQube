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
        current = calc_stack.popleft()
        if not self.is_operator(current):
            if current.startswith('~'):
                value = Decimal(current[1:]) * Decimal(-1)
                result_stack.append(value)
            else:
                result_stack.append(Decimal(current))
        else:
            if len(result_stack) < 2:
                raise ValueError("Invalid expression: insufficient operands for operator '{}'".format(current))
            second_value = result_stack.pop()
            first_value = result_stack.pop()
            if isinstance(first_value, str) and first_value.startswith('~'):
                first_value = Decimal(first_value[1:]) * Decimal(-1)
            if isinstance(second_value, str) and second_value.startswith('~'):
                second_value = Decimal(second_value[1:]) * Decimal(-1)
            result = self._calculate(str(first_value), str(second_value), current)
            result_stack.append(result)
    if len(result_stack) != 1:
        raise ValueError('Invalid expression: could not compute final result')
    return float(result_stack.pop())