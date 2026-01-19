def calculate(self, expression):
    """
        दिए गए पोस्टफ़िक्स एक्सप्रेशन का रिज़ल्ट कैलकुलेट करें।

        :param expression: string, कैलकुलेट करने के लिए पोस्टफ़िक्स एक्सप्रेशन
        :return: float, कैलकुलेट किया गया रिज़ल्ट

        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.calculate("2 + 3 * 4")
        14.0
        """
    self.postfix_stack.clear()
    transformed_expression = self.transform(expression)
    self.prepare(transformed_expression)
    calc_stack = deque(self.postfix_stack.copy())
    result_stack = deque()
    while calc_stack:
        token = calc_stack.popleft()
        if self.is_operator(token):
            if len(result_stack) < 2:
                raise ValueError('Invalid expression: insufficient operands')
            second_value = result_stack.pop()
            first_value = result_stack.pop()
            if token == '~':
                result_stack.append(first_value)
                result_stack.append(str(-Decimal(second_value)))
            else:
                result = self._calculate(first_value, second_value, token)
                result_stack.append(str(result))
        elif token.startswith('~'):
            result_stack.append(str(-Decimal(token[1:])))
        else:
            result_stack.append(token)
    if len(result_stack) != 1:
        raise ValueError('Invalid expression: too many operands')
    return float(Decimal(result_stack.pop()))