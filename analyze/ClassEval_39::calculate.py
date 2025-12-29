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
    result_stack = deque()
    for item in self.postfix_stack:
        if self.is_operator(item):
            if item == '~':
                if result_stack:
                    operand = result_stack.pop()
                    result_stack.append(Decimal(operand) * Decimal(-1))
            elif len(result_stack) >= 2:
                second_value = result_stack.pop()
                first_value = result_stack.pop()
                result = self._calculate(first_value, second_value, item)
                result_stack.append(result)
        else:
            result_stack.append(item)
    self.postfix_stack.clear()
    if result_stack:
        return float(result_stack.pop())
    else:
        return 0.0