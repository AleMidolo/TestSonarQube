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
    i = 0
    while i < len(arr):
        if not self.is_operator(arr[i]):
            if arr[i] == '~':
                i += 1
                start = i
                while i < len(arr) and (not self.is_operator(arr[i])):
                    i += 1
                if start < i:
                    self.postfix_stack.append('~' + ''.join(arr[start:i]))
                continue
            else:
                start = i
                while i < len(arr) and (not self.is_operator(arr[i])):
                    i += 1
                self.postfix_stack.append(''.join(arr[start:i]))
                continue
        else:
            if arr[i] == '(':
                op_stack.append(arr[i])
            elif arr[i] == ')':
                while op_stack and op_stack[-1] != '(':
                    self.postfix_stack.append(op_stack.pop())
                if op_stack:
                    op_stack.pop()
            else:
                while op_stack and op_stack[-1] != '(' and self.compare(arr[i], op_stack[-1]):
                    self.postfix_stack.append(op_stack.pop())
                op_stack.append(arr[i])
            i += 1
    while op_stack:
        self.postfix_stack.append(op_stack.pop())