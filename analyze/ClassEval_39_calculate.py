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
    result_stack = deque()
    for item in self.postfix_stack:
        if self.is_operator(item):
            if item == '~':
                if result_stack:
                    operand = result_stack.pop()
                    result_stack.append(Decimal(0) - Decimal(operand))
            else:
                if len(result_stack) < 2:
                    raise ValueError('Invalid expression: insufficient operands')
                second_value = result_stack.pop()
                first_value = result_stack.pop()
                result = self._calculate(first_value, second_value, item)
                result_stack.append(result)
        else:
            result_stack.append(item)
    if not result_stack:
        raise ValueError('Invalid expression: no result')
    result = float(result_stack.pop())
    self.postfix_stack.clear()
    return result