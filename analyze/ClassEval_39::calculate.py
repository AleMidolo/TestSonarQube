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
    expression = self.transform(expression)
    self.prepare(expression)

    for token in self.postfix_stack:
        if self.is_operator(token):
            second_value = self.postfix_stack.pop()
            first_value = self.postfix_stack.pop()
            result = self._calculate(first_value, second_value, token)
            self.postfix_stack.append(result)
        else:
            self.postfix_stack.append(token)

    return float(self.postfix_stack.pop())