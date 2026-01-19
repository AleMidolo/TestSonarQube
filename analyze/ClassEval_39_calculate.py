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
    for item in self.postfix_stack:
        if self.is_operator(item):
            if item == '~':
                if calc_stack:
                    operand = calc_stack.pop()
                    calc_stack.append(str(-Decimal(operand)))
            else:
                if len(calc_stack) < 2:
                    raise ValueError('Invalid expression: insufficient operands')
                second_value = calc_stack.pop()
                first_value = calc_stack.pop()
                result = self._calculate(first_value, second_value, item)
                calc_stack.append(str(result))
        else:
            calc_stack.append(item)
    if not calc_stack:
        raise ValueError('Invalid expression: no result')
    result = float(Decimal(calc_stack.pop()))
    self.postfix_stack.clear()
    return result