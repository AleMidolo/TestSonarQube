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
        if c.isdigit() or c == '.' or c == '~':
            if c == '~':
                j = i + 1
                while j < len(expression) and (expression[j].isdigit() or expression[j] == '.'):
                    j += 1
                num = expression[i:j]
                self.postfix_stack.append(num)
                i = j
                continue
            else:
                j = i
                while j < len(expression) and (expression[j].isdigit() or expression[j] == '.'):
                    j += 1
                num = expression[i:j]
                self.postfix_stack.append(num)
                i = j
                continue
        elif self.is_operator(c):
            if c == '(':
                operator_stack.append(c)
            elif c == ')':
                while operator_stack and operator_stack[-1] != '(':
                    self.postfix_stack.append(operator_stack.pop())
                if operator_stack:
                    operator_stack.pop()
            else:
                while operator_stack and operator_stack[-1] != '(' and self.compare(c, operator_stack[-1]):
                    self.postfix_stack.append(operator_stack.pop())
                operator_stack.append(c)
            i += 1
        else:
            i += 1
    while operator_stack:
        self.postfix_stack.append(operator_stack.pop())