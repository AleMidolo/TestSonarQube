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
    i = 0
    while i < len(expression):
        c = expression[i]
        if c.isdigit() or c == '~':
            num = c
            while i + 1 < len(expression) and (expression[i + 1].isdigit() or expression[i + 1] == '.'):
                i += 1
                num += expression[i]
            output.append(num)
        elif self.is_operator(c):
            while operator_stack and operator_stack[-1] != '(' and self.compare(c, operator_stack[-1]):
                output.append(operator_stack.pop())
            operator_stack.append(c)
        elif c == '(':
            operator_stack.append(c)
        elif c == ')':
            while operator_stack and operator_stack[-1] != '(':
                output.append(operator_stack.pop())
            operator_stack.pop()
        i += 1
    while operator_stack:
        output.append(operator_stack.pop())
    self.postfix_stack = output