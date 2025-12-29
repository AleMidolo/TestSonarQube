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
    first_index = True
    i = 0
    while i < len(arr):
        if not self.is_operator(arr[i]):
            if first_index:
                first_index = False
                current_index = i
            count += 1
            i += 1
            if i >= len(arr):
                self.postfix_stack.append(''.join(arr[current_index:current_index + count]))
            continue
        elif arr[i] == '(':
            op_stack.append(arr[i])
        elif arr[i] == ')':
            self.postfix_stack.append(''.join(arr[current_index:current_index + count]))
            while op_stack and op_stack[-1] != '(':
                self.postfix_stack.append(op_stack.pop())
            op_stack.pop()
        else:
            if count > 0:
                self.postfix_stack.append(''.join(arr[current_index:current_index + count]))
                count = 0
            current_op = arr[i]
            if current_op == '~':
                if i > 0 and arr[i - 1] == '(':
                    self.postfix_stack.append('0')
                current_op = '-'
            while op_stack and op_stack[-1] != '(' and self.compare(current_op, op_stack[-1]):
                self.postfix_stack.append(op_stack.pop())
            op_stack.append(current_op)
            first_index = True
        i += 1
    if count > 1 or (count == 1 and (not self.is_operator(arr[-1]))):
        self.postfix_stack.append(''.join(arr[current_index:current_index + count]))
    while op_stack:
        self.postfix_stack.append(op_stack.pop())