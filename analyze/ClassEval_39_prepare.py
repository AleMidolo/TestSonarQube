def prepare(self, expression):
    """
        Prepara un'espressione in notazione infissa per la conversione in notazione postfissa.
        :param expression: stringa, l'espressione infissa da preparare
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
                while current_index < len(arr) and (arr[current_index].isdigit() or arr[current_index] == '.'):
                    current_index += 1
                self.postfix_stack.append(''.join(arr[count:current_index]))
            else:
                count = current_index
                current_index += 1
                while current_index < len(arr) and (arr[current_index].isdigit() or arr[current_index] == '.'):
                    current_index += 1
                self.postfix_stack.append(''.join(arr[count:current_index]))
        else:
            if c == ')':
                while op_stack and op_stack[-1] != '(':
                    self.postfix_stack.append(op_stack.pop())
                op_stack.pop()
            elif not op_stack:
                op_stack.append(c)
            elif c == '(':
                op_stack.append(c)
            elif op_stack[-1] == '(':
                op_stack.append(c)
            elif self.compare(c, op_stack[-1]):
                op_stack.append(c)
            else:
                while op_stack and op_stack[-1] != '(' and (not self.compare(c, op_stack[-1])):
                    self.postfix_stack.append(op_stack.pop())
                op_stack.append(c)
            current_index += 1
    while op_stack:
        self.postfix_stack.append(op_stack.pop())