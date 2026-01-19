def calculate(self, expression):
    """
        Calcular el resultado de la expresión en notación postfija dada
        :param expression: cadena, la expresión en notación postfija a calcular
        :return: float, el resultado calculado
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.calculate("2 + 3 * 4")
        14.0

        """
    transformed_expression = self.transform(expression)
    self.postfix_stack.clear()
    self.prepare(transformed_expression)
    calc_stack = deque()
    for item in self.postfix_stack:
        if self.is_operator(item):
            if item == '~':
                if calc_stack:
                    operand = calc_stack.pop()
                    calc_stack.append(str(-Decimal(operand)))
            elif len(calc_stack) >= 2:
                second_value = calc_stack.pop()
                first_value = calc_stack.pop()
                result = self._calculate(first_value, second_value, item)
                calc_stack.append(str(result))
        else:
            calc_stack.append(item)
    if calc_stack:
        result = Decimal(calc_stack.pop())
        return float(result)
    else:
        return 0.0