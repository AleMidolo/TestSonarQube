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
    transformed_expr = self.transform(expression)
    self.prepare(transformed_expr)
    result_stack = deque()
    for token in self.postfix_stack:
        if self.is_operator(token):
            if token == '~':
                if len(result_stack) < 1:
                    raise ValueError('Invalid expression: insufficient operands for unary minus')
                operand = result_stack.pop()
                result_stack.append(-Decimal(operand))
            else:
                if len(result_stack) < 2:
                    raise ValueError('Invalid expression: insufficient operands for binary operator')
                second_value = result_stack.pop()
                first_value = result_stack.pop()
                result = self._calculate(first_value, second_value, token)
                result_stack.append(result)
        else:
            result_stack.append(token)
    if len(result_stack) != 1:
        raise ValueError('Invalid expression: could not compute final result')
    result = float(result_stack.pop())
    return result