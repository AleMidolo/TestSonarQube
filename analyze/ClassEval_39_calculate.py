def calculate(self, expression):
    """
        Calcular el resultado de la expresión en notación postfija dada
        :param expression: cadena, la expresión en notación postfija a calcular
        :return: float, el resultado calculado
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.calculate("2 + 3 * 4")
        14.0

        """
    transformed_expr = self.transform(expression)
    self.postfix_stack.clear()
    self.prepare(transformed_expr)
    result_stack = deque()
    for token in self.postfix_stack:
        if self.is_operator(token):
            if token == '~':
                if not result_stack:
                    raise ValueError('Invalid expression: unary minus without operand')
                operand = result_stack.pop()
                result_stack.append(-Decimal(operand))
            else:
                if len(result_stack) < 2:
                    raise ValueError('Invalid expression: insufficient operands for operator')
                second_value = result_stack.pop()
                first_value = result_stack.pop()
                result = self._calculate(first_value, second_value, token)
                result_stack.append(result)
        else:
            result_stack.append(token)
    if len(result_stack) != 1:
        raise ValueError('Invalid expression: could not compute final result')
    return float(result_stack.pop())