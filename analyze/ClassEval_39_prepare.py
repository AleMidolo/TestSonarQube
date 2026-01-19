def prepare(self, expression):
    """
        Prepara la expresión en notación infija para su conversión a notación postfija
        :param expression: cadena, la expresión infija que se va a preparar
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.prepare("2+3*4")

        expression_calculator.postfix_stack = ['2', '3', '4', '*', '+']
        """
    op_stack = deque()
    arr = list(expression)
    current_index = 0
    count = 0
    while current_index < len(arr):
        current_char = arr[current_index]
        if current_char.isdigit() or current_char == '.' or current_char == '~':
            if current_char == '~':
                count = current_index
                current_index += 1
                temp = []
                while current_index < len(arr):
                    c = arr[current_index]
                    if c.isdigit() or c == '.':
                        temp.append(c)
                        current_index += 1
                    else:
                        break
                self.postfix_stack.append('~' + ''.join(temp))
                continue
            else:
                count = current_index
                temp = []
                while current_index < len(arr):
                    c = arr[current_index]
                    if c.isdigit() or c == '.':
                        temp.append(c)
                        current_index += 1
                    else:
                        break
                self.postfix_stack.append(''.join(temp))
                continue
        elif self.is_operator(current_char):
            if current_char == '(':
                op_stack.append(current_char)
            elif current_char == ')':
                while op_stack and op_stack[-1] != '(':
                    self.postfix_stack.append(op_stack.pop())
                op_stack.pop()
            else:
                while op_stack and op_stack[-1] != '(' and self.compare(current_char, op_stack[-1]):
                    self.postfix_stack.append(op_stack.pop())
                op_stack.append(current_char)
            current_index += 1
            continue
        current_index += 1
    while op_stack:
        self.postfix_stack.append(op_stack.pop())