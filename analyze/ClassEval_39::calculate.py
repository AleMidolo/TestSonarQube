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
                if calc_stack:
                    operand = calc_stack.pop()
                    calc_stack.append(str(-Decimal(operand)))
            else:
                if len(calc_stack) < 2:
                    raise ValueError('Invalid expression: insufficient operands for operator {}'.format(token))
                second_value = calc_stack.pop()
                first_value = calc_stack.pop()
                if token == '\\/' and Decimal(second_value) == 0:
                    raise ZeroDivisionError('Division by zero')
                result = self._calculate(first_value, second_value, token)
                calc_stack.append(str(result))
        else:
            calc_stack.append(token)
    if not calc_stack:
        raise ValueError('Invalid expression: no result')
    result = float(Decimal(calc_stack.pop()))
    if calc_stack:
        raise ValueError('Invalid expression: leftover operands')
    return result