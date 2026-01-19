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
    calc_stack = deque()
    for token in self.postfix_stack:
        if self.is_operator(token):
            if token == '~':
                if calc_stack:
                    operand = calc_stack.pop()
                    calc_stack.append(str(-Decimal(operand)))
            else:
                if len(calc_stack) < 2:
                    raise ValueError('Invalid expression: insufficient operands')
                second = calc_stack.pop()
                first = calc_stack.pop()
                result = self._calculate(first, second, token)
                calc_stack.append(str(result))
        else:
            calc_stack.append(token)
    if not calc_stack:
        raise ValueError('Invalid expression: no result')
    result = Decimal(calc_stack.pop())
    self.postfix_stack.clear()
    return float(result)