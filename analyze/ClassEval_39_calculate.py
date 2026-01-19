def calculate(self, expression):
    """
        Calcola il risultato dell'espressione postfix fornita
        :param expression: stringa, l'espressione postfix da calcolare
        :return: float, il risultato calcolato
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
                    raise ValueError('Invalid expression: insufficient operands for operator {}'.format(token))
                second_value = calc_stack.pop()
                first_value = calc_stack.pop()
                result = self._calculate(first_value, second_value, token)
                calc_stack.append(str(result))
        else:
            calc_stack.append(token)
    if len(calc_stack) != 1:
        raise ValueError('Invalid expression: multiple values remaining in calculation stack')
    result_decimal = Decimal(calc_stack.pop())
    return float(result_decimal)