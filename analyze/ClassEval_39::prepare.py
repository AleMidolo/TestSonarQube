def prepare(self, expression):
        """
        准备中缀表达式以便转换为后缀表示法
        :param expression: 字符串，要准备的中缀表达式
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.prepare("2+3*4")

        expression_calculator.postfix_stack = ['2', '3', '4', '*', '+']
        """
        operator_stack = []
        for char in expression:
            if char.isdigit() or char == '~':
                self.postfix_stack.append(char)
            elif self.is_operator(char):
                while (operator_stack and operator_stack[-1] != '(' and
                       self.compare(char, operator_stack[-1])):
                    self.postfix_stack.append(operator_stack.pop())
                operator_stack.append(char)
            elif char == '(':
                operator_stack.append(char)
            elif char == ')':
                while operator_stack and operator_stack[-1] != '(':
                    self.postfix_stack.append(operator_stack.pop())
                operator_stack.pop()  # pop the '('
        
        while operator_stack:
            self.postfix_stack.append(operator_stack.pop())