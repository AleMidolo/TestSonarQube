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
                count = current_index + 1
                temp = ['-']
                while count < len(arr) and (arr[count].isdigit() or arr[count] == '.'):
                    temp.append(arr[count])
                    count += 1
                temp_str = ''.join(temp)
                self.postfix_stack.append(temp_str)
            else:
                count = current_index
                temp = []
                while count < len(arr) and (arr[count].isdigit() or arr[count] == '.'):
                    temp.append(arr[count])
                    count += 1
                temp_str = ''.join(temp)
                self.postfix_stack.append(temp_str)
            current_index = count
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
    while op_stack:
        self.postfix_stack.append(op_stack.pop())