def prepare(self, expression):
    """
        इनफिक्स अभिव्यक्ति को पोस्टफिक्स नोटेशन में रूपांतरित करने के लिए तैयार करें
        :param expression: स्ट्रिंग, तैयार की जाने वाली इनफिक्स अभिव्यक्ति
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.prepare("2+3*4")

        expression_calculator.postfix_stack = ['2', '3', '4', '*', '+']
        """
    operator_stack = deque()
    self.postfix_stack.clear()
    i = 0
    while i < len(expression):
        c = expression[i]
        if c == ' ':
            i += 1
            continue
        if c == '(':
            operator_stack.append(c)
        elif c == ')':
            while operator_stack and operator_stack[-1] != '(':
                self.postfix_stack.append(operator_stack.pop())
            operator_stack.pop()
        elif self.is_operator(c):
            while operator_stack and operator_stack[-1] != '(' and self.compare(c, operator_stack[-1]):
                self.postfix_stack.append(operator_stack.pop())
            operator_stack.append(c)
        else:
            operand = ''
            if c == '~':
                operand += '-'
                i += 1
                c = expression[i]
            while i < len(expression) and (expression[i].isdigit() or expression[i] == '.' or expression[i] == 'E' or (expression[i] == 'e')):
                operand += expression[i]
                i += 1
            i -= 1
            self.postfix_stack.append(operand)
        i += 1
    while operator_stack:
        self.postfix_stack.append(operator_stack.pop())