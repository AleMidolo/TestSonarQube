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
                if not calc_stack:
                    raise ValueError('Invalid expression: missing operand for unary minus')
                operand = calc_stack.pop()
                result = Decimal(0) - Decimal(operand)
                calc_stack.append(str(result))
            else:
                if len(calc_stack) < 2:
                    raise ValueError(f"Invalid expression: insufficient operands for operator '{token}'")
                second_value = calc_stack.pop()
                first_value = calc_stack.pop()
                if token == '\\/' and Decimal(second_value) == 0:
                    raise ZeroDivisionError('Division by zero')
                result = self._calculate(first_value, second_value, token)
                calc_stack.append(str(result))
        else:
            calc_stack.append(token)
    if len(calc_stack) != 1:
        raise ValueError('Invalid expression: malformed postfix notation')
    return float(calc_stack.pop())