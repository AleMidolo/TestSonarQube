class Calculator: 
    def __init__(self):
        """
        Initialize the operations performed by the five operators'+','-','*','/','^'
        """
        self.operators = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y,
            '^': lambda x, y: x ** y
        }

    def calculate(self, expression):
        """
        Calculate the value of a given expression
        :param expression: string, given expression
        :return:If successful, returns the value of the expression; otherwise, returns None
        >>> calculator = Calculator()
        >>> calculator.calculate('1+2-3')
        0.0
        """
    
        operand_stack = []
        operator_stack = []
        num_buffer = ''
    
        for char in expression:
            if char.isdigit() or char == '.':
                num_buffer += char
            else:
                if num_buffer:
                    operand_stack.append(float(num_buffer))
                    num_buffer = ''
    
                if char in '+-*/^':
                    while (
                            operator_stack and
                            operator_stack[-1] != '(' and
                            self.precedence(
                                operator_stack[-1]) >= self.precedence(char)
                    ):
                        operand_stack, operator_stack = self.apply_operator(
                            operand_stack, operator_stack)
    
                    operator_stack.append(char)
                elif char == '(':
                    operator_stack.append(char)
                elif char == ')':
                    while operator_stack and operator_stack[-1] != '(':
                        operand_stack, operator_stack = self.apply_operator(
                            operand_stack, operator_stack)
    
                    operator_stack.pop()
    
        if num_buffer:
            operand_stack.append(float(num_buffer))
    
        while operator_stack:
            operand_stack, operator_stack = self.apply_operator(
                operand_stack, operator_stack)
    
        return operand_stack[-1] if operand_stack else None
    
    def apply_operator(self, operand_stack, operator_stack):
        """
        Use the operator at the top of the operator stack to perform the operation on the two numbers at the top of the operator stack, and store the results at the top of the operator stack
        :param operand_stack:list
        :param operator_stack:list
        :return: the updated operand_stack and operator_stack
        >>> calculator = Calculator()
        >>> calculator.apply_operator([1, 2, 3], ['+', '-'])
        ([1, -1], ['-'])
        """
    
        operator = operator_stack.pop()
        if operator == '^':
            operand2 = operand_stack.pop()
            operand1 = operand_stack.pop()
            result = self.operators[operator](operand1, operand2)
            operand_stack.append(result)
        else:
            operand2 = operand_stack.pop()
            operand1 = operand_stack.pop()
            result = self.operators[operator](operand1, operand2)
            operand_stack.append(result)
        return operand_stack, operator_stack
    
    def precedence(self, operator):
        """
        निर्दिष्ट ऑपरेटर की प्राथमिकता लौटाता है, जहाँ उच्च प्राथमिकता का अर्थ है अधिक असाइनमेंट। '^' की प्राथमिकता '/' और '*' से अधिक है, और '/' और '*' की प्राथमिकता '+' और '-' से अधिक है।
        :param operator: स्ट्रिंग, दिया गया ऑपरेटर
        :return: int, दिए गए ऑपरेटर की प्राथमिकता, अन्यथा 0 लौटाएं
        >>> calculator = Calculator()
        >>> calculator.precedence('+')
        1
        >>> calculator.precedence('^')
        3
        """
        if operator == '+':
            return 1
        elif operator == '-':
            return 1
        elif operator == '*':
            return 2
        elif operator == '/':
            return 2
        elif operator == '^':
            return 3
        return 0