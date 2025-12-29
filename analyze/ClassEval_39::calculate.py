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
        if not self.is_operator(item):
            if item.startswith('~'):
                calc_stack.append(str(-Decimal(item[1:])))
            else:
                calc_stack.append(item)
        else:
            second_value = calc_stack.pop()
            first_value = calc_stack.pop()
            result = self._calculate(first_value, second_value, item)
            calc_stack.append(str(result))
    if len(calc_stack) != 1:
        raise ValueError('Invalid expression: calculation stack has more than one item')
    return float(calc_stack.pop())