class Calculator:
    def __init__(self):
        self.operators = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y,
            '^': lambda x, y: x ** y
        }
        self.precedences = {
            '+': 1,
            '-': 1,
            '*': 2,
            '/': 2,
            '^': 3
        }

    def calculate(self, expression):
        operand_stack = []
        operator_stack = []
        num_buffer = ''

        for char in expression:
            if self.is_number(char):
                num_buffer += char
            else:
                if num_buffer:
                    operand_stack.append(float(num_buffer))
                    num_buffer = ''

                if char in self.operators:
                    self.process_operator(char, operand_stack, operator_stack)
                elif char == '(':
                    operator_stack.append(char)
                elif char == ')':
                    self.process_parenthesis(operand_stack, operator_stack)

        if num_buffer:
            operand_stack.append(float(num_buffer))

        while operator_stack:
            operand_stack, operator_stack = self.apply_operator(operand_stack, operator_stack)

        return operand_stack[-1] if operand_stack else None

    def is_number(self, char):
        return char.isdigit() or char == '.'

    def process_operator(self, char, operand_stack, operator_stack):
        while (
                operator_stack and
                operator_stack[-1] != '(' and
                self.precedence(operator_stack[-1]) >= self.precedence(char)
        ):
            operand_stack, operator_stack = self.apply_operator(operand_stack, operator_stack)

        operator_stack.append(char)

    def process_parenthesis(self, operand_stack, operator_stack):
        while operator_stack and operator_stack[-1] != '(':
            operand_stack, operator_stack = self.apply_operator(operand_stack, operator_stack)
        operator_stack.pop()

    def precedence(self, operator):
        return self.precedences.get(operator, 0)

    def apply_operator(self, operand_stack, operator_stack):
        operator = operator_stack.pop()
        operand2 = operand_stack.pop()
        operand1 = operand_stack.pop()
        result = self.operators[operator](operand1, operand2)
        operand_stack.append(result)
        return operand_stack, operator_stack