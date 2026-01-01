def prepare(self, expression):
    """
        准备中缀表达式以便转换为后缀表示法
        :param expression: 字符串，要准备的中缀表达式
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.prepare("2+3*4")

        expression_calculator.postfix_stack = ['2', '3', '4', '*', '+']
        """
    op_stack = deque()
    arr = list(expression)
    current_index = 0
    count = len(arr)
    while current_index < count:
        current_char = arr[current_index]
        if self.is_operator(current_char):
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
        else:
            sb = []
            is_negative = False
            if current_char == '~':
                is_negative = True
                current_index += 1
                if current_index < count:
                    current_char = arr[current_index]
            while current_index < count:
                current_char = arr[current_index]
                if not self.is_operator(current_char):
                    sb.append(current_char)
                    current_index += 1
                else:
                    break
            number_str = ''.join(sb)
            if is_negative:
                number_str = '~' + number_str
            self.postfix_stack.append(number_str)
    while op_stack:
        self.postfix_stack.append(op_stack.pop())