def prepare(self, expression):
    """
        इनफिक्स अभिव्यक्ति को पोस्टफिक्स नोटेशन में रूपांतरित करने के लिए तैयार करें
        :param expression: स्ट्रिंग, तैयार की जाने वाली इनफिक्स अभिव्यक्ति
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.prepare("2+3*4")

        expression_calculator.postfix_stack = ['2', '3', '4', '*', '+']
        """
    op_stack = deque()
    arr = list(expression)
    current_index = 0
    count = 0
    while current_index < len(arr):
        c = arr[current_index]
        current_index += 1
        if c.isdigit():
            count += 1
            if count > 1:
                t = self.postfix_stack.pop() + c
                self.postfix_stack.append(t)
            else:
                self.postfix_stack.append(c)
            if current_index >= len(arr):
                while op_stack:
                    self.postfix_stack.append(op_stack.pop())
        else:
            count = 0
            if c == ')':
                while op_stack:
                    op = op_stack.pop()
                    if op == '(':
                        break
                    else:
                        self.postfix_stack.append(op)
            elif not op_stack:
                op_stack.append(c)
            elif c == '(':
                op_stack.append(c)
            else:
                while op_stack:
                    op = op_stack[-1]
                    if self.compare(c, op):
                        self.postfix_stack.append(op_stack.pop())
                    else:
                        break
                op_stack.append(c)
    while op_stack:
        self.postfix_stack.append(op_stack.pop())