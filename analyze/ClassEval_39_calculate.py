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
    eval_stack = deque()
    for token in self.postfix_stack:
        if self.is_operator(token):
            if token == '~':
                if not eval_stack:
                    raise ValueError('Invalid expression: missing operand for unary minus')
                operand = eval_stack.pop()
                result = Decimal(0) - Decimal(operand)
                eval_stack.append(str(result))
            else:
                if len(eval_stack) < 2:
                    raise ValueError('Invalid expression: insufficient operands for operator {}'.format(token))
                second_value = eval_stack.pop()
                first_value = eval_stack.pop()
                result = self._calculate(first_value, second_value, token)
                eval_stack.append(str(result))
        else:
            eval_stack.append(token)
    if len(eval_stack) != 1:
        raise ValueError('Invalid expression: evaluation stack has {} elements instead of 1'.format(len(eval_stack)))
    return float(eval_stack.pop())