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
    current_op = ''
    while current_index < len(arr):
        c = arr[current_index]
        current_index += 1
        if c != ' ':
            if self.is_operator(c):
                if count > 0:
                    self.postfix_stack.append(current_op)
                    current_op = ''
                    count = 0
                if c == '(':
                    op_stack.append(c)
                elif c == ')':
                    while op_stack and op_stack[-1] != '(':
                        self.postfix_stack.append(op_stack.pop())
                    if op_stack and op_stack[-1] == '(':
                        op_stack.pop()
                else:
                    while op_stack and op_stack[-1] != '(' and self.compare(c, op_stack[-1]):
                        self.postfix_stack.append(op_stack.pop())
                    op_stack.append(c)
            else:
                current_op += c
                count += 1
    if count > 0:
        self.postfix_stack.append(current_op)
    while op_stack:
        self.postfix_stack.append(op_stack.pop())