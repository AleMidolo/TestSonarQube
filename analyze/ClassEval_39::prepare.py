def prepare(self, expression):
    """
        इनफिक्स अभिव्यक्ति को पोस्टफिक्स नोटेशन में रूपांतरित करने के लिए तैयार करें
        :param expression: स्ट्रिंग, तैयार की जाने वाली इनफिक्स अभिव्यक्ति
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.prepare("2+3*4")

        expression_calculator.postfix_stack = ['2', '3', '4', '*', '+']
        """
    operator_stack = deque()
    output = []
    for char in expression:
        if char.isdigit() or char == '~':
            output.append(char)
        elif self.is_operator(char):
            while operator_stack and operator_stack[-1] != '(' and self.compare(char, operator_stack[-1]):
                output.append(operator_stack.pop())
            operator_stack.append(char)
        elif char == '(':
            operator_stack.append(char)
        elif char == ')':
            while operator_stack and operator_stack[-1] != '(':
                output.append(operator_stack.pop())
            operator_stack.pop()
    while operator_stack:
        output.append(operator_stack.pop())
    self.postfix_stack = output