def calculate(self, expression):
    """
        Calcular el resultado de la expresión en notación postfija dada
        :param expression: cadena, la expresión en notación postfija a calcular
        :return: float, el resultado calculado
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.calculate("2 + 3 * 4")
        14.0

        """
    self.postfix_stack.clear()
    transformed_expression = self.transform(expression)
    self.prepare(transformed_expression)
    result_stack = deque()
    for token in self.postfix_stack:
        if self.is_operator(token):
            if token == '~':
                if result_stack:
                    operand = result_stack.pop()
                    result_stack.append(Decimal(operand) * Decimal(-1))
            else:
                if len(result_stack) < 2:
                    raise ValueError('Invalid expression: insufficient operands for operator {}'.format(token))
                second_value = result_stack.pop()
                first_value = result_stack.pop()
                if token == '\\/' and Decimal(second_value) == 0:
                    raise ZeroDivisionError('Division by zero')
                result = self._calculate(first_value, second_value, token)
                result_stack.append(result)
        elif token.startswith('~'):
            result_stack.append(Decimal(token[1:]) * Decimal(-1))
        else:
            result_stack.append(Decimal(token))
    if len(result_stack) != 1:
        raise ValueError('Invalid expression: too many operands or operators')
    return float(result_stack.pop())