def calculate(self, expression):
    """
        计算给定后缀表达式的结果
        :param expression: 字符串，要计算的后缀表达式
        :return: 浮点数，计算结果
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
            if token in {'+', '-', '*', '\\/', '%'}:
                if len(calc_stack) < 2:
                    raise ValueError('Invalid expression: insufficient operands')
                second_value = calc_stack.pop()
                first_value = calc_stack.pop()
                if first_value == '~':
                    first_value = '-0'
                elif isinstance(first_value, str) and first_value.startswith('~'):
                    first_value = '-' + first_value[1:]
                if second_value == '~':
                    second_value = '-0'
                elif isinstance(second_value, str) and second_value.startswith('~'):
                    second_value = '-' + second_value[1:]
                result = self._calculate(first_value, second_value, token)
                calc_stack.append(str(result))
            elif token in {'(', ')'}:
                continue
        elif token == '~':
            calc_stack.append('~')
        elif isinstance(token, str) and token.startswith('~'):
            calc_stack.append('-' + token[1:])
        else:
            calc_stack.append(token)
    if len(calc_stack) != 1:
        raise ValueError('Invalid expression: multiple values in result stack')
    result = calc_stack.pop()
    if result == '~':
        result = '-0'
    elif isinstance(result, str) and result.startswith('~'):
        result = '-' + result[1:]
    return float(Decimal(result))