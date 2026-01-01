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
    calc_stack = deque(self.postfix_stack.copy())
    operand_stack = deque()
    while calc_stack:
        token = calc_stack.popleft()
        if self.is_operator(token):
            if token == '~':
                if not operand_stack:
                    raise ValueError('Invalid expression: missing operand for unary minus')
                operand = operand_stack.pop()
                result = -Decimal(operand)
                operand_stack.append(str(result))
            else:
                if len(operand_stack) < 2:
                    raise ValueError('Invalid expression: insufficient operands for operator {}'.format(token))
                second_value = operand_stack.pop()
                first_value = operand_stack.pop()
                result = self._calculate(first_value, second_value, token)
                operand_stack.append(str(result))
        else:
            operand_stack.append(token)
    if len(operand_stack) != 1:
        raise ValueError('Invalid expression: multiple values remaining after calculation')
    result_decimal = Decimal(operand_stack.pop())
    return float(result_decimal)