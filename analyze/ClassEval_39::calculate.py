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
    for item in self.postfix_stack:
        if not self.is_operator(item):
            if item.startswith('~'):
                calc_stack.append(str(-Decimal(item[1:])))
            else:
                calc_stack.append(item)
        else:
            if len(calc_stack) < 2:
                raise ValueError('Invalid expression: insufficient operands')
            second_value = calc_stack.pop()
            first_value = calc_stack.pop()
            result = self._calculate(first_value, second_value, item)
            calc_stack.append(str(result))
    if len(calc_stack) != 1:
        raise ValueError('Invalid expression: too many operands')
    return float(calc_stack.pop())