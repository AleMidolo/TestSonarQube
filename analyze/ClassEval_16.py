class Calculator:
    def __init__(self):
        self.operators = {
            '+': self.add,
            '-': self.subtract,
            '*': self.multiply,
            '/': self.divide,
            '^': self.power
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
                    self.push_operand(operand_stack, num_buffer)
                    num_buffer = ''

                if self.is_operator(char):
                    self.process_operator(char, operand_stack, operator_stack)
                elif char == '(':
                    operator_stack.append(char)
                elif char == ')':
                    self.process_parenthesis(operand_stack, operator_stack)

        if num_buffer:
            self.push_operand(operand_stack, num_buffer)

        while operator_stack:
            self.apply_operator(operand_stack, operator_stack)

        return operand_stack[-1] if operand_stack else None

    def precedence(self, operator):
        precedences = {
            '+': 1,
            '-': 1,
            '*': 2,
            '/': 2,
            '^': 3
        }
        return precedences.get(operator, 0)

    def apply_operator(self, operand_stack, operator_stack):
        operator = operator_stack.pop()
        operand2 = operand_stack.pop()
        operand1 = operand_stack.pop()
        result = self.operators[operator](operand1, operand2)
        operand_stack.append(result)

    def is_number(self, char):
        return char.isdigit() or char == '.'

    def is_operator(self, char):
        return char in self.operators

    def push_operand(self, operand_stack, num_buffer):
        operand_stack.append(float(num_buffer))

    def process_operator(self, char, operand_stack, operator_stack):
        while (
                operator_stack and
                operator_stack[-1] != '(' and
                self.precedence(operator_stack[-1]) >= self.precedence(char)
        ):
            self.apply_operator(operand_stack, operator_stack)
        operator_stack.append(char)

    def process_parenthesis(self, operand_stack, operator_stack):
        while operator_stack and operator_stack[-1] != '(':
            self.apply_operator(operand_stack, operator_stack)
        operator_stack.pop()

    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        return x / y

    def power(self, x, y):
        return x ** y