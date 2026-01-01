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
    calc_stack = deque()
    for token in self.postfix_stack:
        if self.is_operator(token):
            if token == '~':
                if not calc_stack:
                    raise ValueError('Invalid expression: missing operand for unary minus')
                operand = calc_stack.pop()
                result = Decimal(0) - Decimal(operand)
                calc_stack.append(str(result))
            else:
                if len(calc_stack) < 2:
                    raise ValueError(f"Invalid expression: insufficient operands for operator '{token}'")
                second_value = calc_stack.pop()
                first_value = calc_stack.pop()
                result = self._calculate(first_value, second_value, token)
                calc_stack.append(str(result))
        else:
            calc_stack.append(token)
    if len(calc_stack) != 1:
        raise ValueError(f'Invalid expression: calculation resulted in {len(calc_stack)} values instead of 1')
    result_decimal = Decimal(calc_stack.pop())
    return float(result_decimal)