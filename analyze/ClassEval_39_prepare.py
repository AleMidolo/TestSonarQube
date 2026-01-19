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
    while current_index < len(arr):
        c = arr[current_index]
        if c.isdigit() or c == '.' or c == '~':
            if c == '~':
                count = current_index
                current_index += 1
                while current_index < len(arr):
                    char = arr[current_index]
                    if char.isdigit() or char == '.':
                        current_index += 1
                    else:
                        break
                operand = ''.join(arr[count:current_index])
                self.postfix_stack.append(operand)
                continue
            else:
                count = current_index
                current_index += 1
                while current_index < len(arr):
                    char = arr[current_index]
                    if char.isdigit() or char == '.':
                        current_index += 1
                    else:
                        break
                operand = ''.join(arr[count:current_index])
                self.postfix_stack.append(operand)
                continue
        elif self.is_operator(c):
            if c == '(':
                op_stack.append(c)
            elif c == ')':
                while op_stack and op_stack[-1] != '(':
                    self.postfix_stack.append(op_stack.pop())
                op_stack.pop()
            else:
                while op_stack and op_stack[-1] != '(' and self.compare(c, op_stack[-1]):
                    self.postfix_stack.append(op_stack.pop())
                op_stack.append(c)
            current_index += 1
        else:
            current_index += 1
    while op_stack:
        self.postfix_stack.append(op_stack.pop())