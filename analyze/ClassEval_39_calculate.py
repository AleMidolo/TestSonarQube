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
    tokens = expression.split()
    for token in tokens:
        if self.is_operator(token):
            second_value = self.postfix_stack.pop()
            first_value = self.postfix_stack.pop()
            result = self._calculate(first_value, second_value, token)
            self.postfix_stack.append(result)
        else:
            self.postfix_stack.append(token)
    return float(self.postfix_stack.pop())