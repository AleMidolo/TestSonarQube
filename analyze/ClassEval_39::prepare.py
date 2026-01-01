def prepare(self, expression):
    """
        Prepare the infix expression for conversion to postfix notation
        :param expression: string, the infix expression to be prepared
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.prepare("2+3*4")
        expression_calculator.postfix_stack = ['2', '3', '4', '*', '+']
        """
    op_stack = deque()
    arr = list(expression)
    current_index = 0
    count = 0
    current_op = ''
    while count < len(arr):
        current_op = arr[count]
        if self.is_operator(current_op):
            if current_op == '(':
                op_stack.append(current_op)
            elif current_op == ')':
                while op_stack and op_stack[-1] != '(':
                    self.postfix_stack.append(op_stack.pop())
                op_stack.pop()
            else:
                while op_stack and op_stack[-1] != '(' and self.compare(current_op, op_stack[-1]):
                    self.postfix_stack.append(op_stack.pop())
                op_stack.append(current_op)
        elif current_op != '~':
            current_index = count
            if current_op.isdigit():
                while count < len(arr) - 1 and (arr[count + 1].isdigit() or arr[count + 1] == '.'):
                    count += 1
                if count >= current_index:
                    num_str = ''.join(arr[current_index:count + 1])
                    self.postfix_stack.append(num_str)
        else:
            while count < len(arr) - 1 and (arr[count + 1].isdigit() or arr[count + 1] == '.' or arr[count + 1] == '~'):
                count += 1
            if count >= current_index:
                num_str = ''.join(arr[current_index:count + 1])
                self.postfix_stack.append(num_str)
        count += 1
    while op_stack:
        self.postfix_stack.append(op_stack.pop())