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
            if not self.is_operator(char):
                self.postfix_stack.append(char)
            else:
                while (operator_stack and 
                       self.compare(char, operator_stack[-1])):
                    self.postfix_stack.append(operator_stack.pop())
                operator_stack.append(char)

        while operator_stack:
            self.postfix_stack.append(operator_stack.pop())