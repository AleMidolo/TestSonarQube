def calculate(self, expression):
    """
    दिए गए पोस्टफ़िक्स एक्सप्रेशन का रिज़ल्ट कैलकुलेट करें।

    :param expression: string, कैलकुलेट करने के लिए पोस्टफ़िक्स एक्सप्रेशन
    :return: float, कैलकुलेट किया गया रिज़ल्ट

    >>> expression_calculator = ExpressionCalculator()
    >>> expression_calculator.calculate("2 + 3 * 4")
    14.0
    """
    
    op_stack = deque()
    tokens = expression.split()
    
    for token in tokens:
        if not self.is_operator(token):
            op_stack.append(token)
        else:
            second_value = op_stack.pop()
            first_value = op_stack.pop()
            result = self._calculate(first_value, second_value, token)
            op_stack.append(str(result))
    
    return float(op_stack.pop())