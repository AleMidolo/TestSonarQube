import re
from collections import deque
from decimal import Decimal

class ExpressionCalculator: 
    def __init__(self):
        """
        Initialize the expression calculator
        """
        self.postfix_stack = deque()
        self.operat_priority = [0, 3, 2, 1, -1, 1, 0, 2]

    def calculate(self, expression):
        """
        Calculate the result of the given postfix expression
        :param expression: string, the postfix expression to be calculated
        :return: float, the calculated result
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.calculate("2 + 3 * 4")
        14.0
        """
        self.prepare(self.transform(expression))
        result_stack = deque()
        self.postfix_stack.reverse()

        while self.postfix_stack:
            current_op = self.postfix_stack.pop()
            if not self.is_operator(current_op):
                current_op = current_op.replace("~", "-")
                result_stack.append(current_op)
            else:
                second_value = result_stack.pop()
                first_value = result_stack.pop()
                first_value = first_value.replace("~", "-")
                second_value = second_value.replace("~", "-")
                temp_result = self._calculate(first_value, second_value, current_op)
                result_stack.append(str(temp_result))

        return float(eval("*".join(result_stack)))

    @staticmethod
    def is_operator(c):
        """
            Check if a character is an operator in {'+', '-', '*', '\/', '(', ')', '%'}
            :param c: string, the character to be checked
            :return: bool, True if the character is an operator, False otherwise
            >>> expression_calculator = ExpressionCalculator()
            >>> expression_calculator.is_operator("+")
            True
        """
        return c in {'+', '-', '*', '\/', '(', ')', '%'}

    def compare(self, cur, peek):
        """
        Compare the precedence of two operators
        :param cur: string, the current operator
        :param peek: string, the operator at the top of the operator stack
        :return: bool, True if the current operator has higher or equal precedence, False otherwise
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.compare("+", "-")
        True
        """
        if cur == '%':
            cur = '\/'
        if peek == '%':
            peek = '\/'
        return self.operat_priority[ord(peek) - 40] >= self.operat_priority[ord(cur) - 40]

    @staticmethod
    def _calculate(first_value, second_value, current_op):
        """
            Perform the mathematical calculation based on the given operands and operator
            :param first_value: string, the first operand
            :param second_value: string, the second operand
            :param current_op: string, the operator
            :return: decimal.Decimal, the calculated result
            >>> expression_calculator = ExpressionCalculator()
            >>> expression_calculator._calculate("2", "3", "+")
            5.0
        """
        if current_op == '+':
            return Decimal(first_value) + Decimal(second_value)
        elif current_op == '-':
            return Decimal(first_value) - Decimal(second_value)
        elif current_op == '*':
            return Decimal(first_value) * Decimal(second_value)
        elif current_op == '\/':
            return Decimal(first_value) / Decimal(second_value)
        elif current_op == '%':
            return Decimal(first_value) % Decimal(second_value)
        else:
            raise ValueError("Unexpected operator: {}".format(current_op))

    @staticmethod
    def transform(expression):
        """
            Transform the infix expression to a format suitable for conversion
            :param expression: string, the infix expression to be transformed
            :return: string, the transformed expression
            >>> expression_calculator = ExpressionCalculator()
            >>> expression_calculator.transform("2 + 3 * 4")
            "2+3*4"
        """
        expression = re.sub(r"\\s+", "", expression)
        expression = re.sub(r"=$", "", expression)
        arr = list(expression)

        for i, c in enumerate(arr):
            if c == '-':
                if i == 0:
                    arr[i] = '~'
                else:
                    prev_c = arr[i - 1]
                    if prev_c in {'+', '-', '*', '\/', '(', 'E', 'e'}:
                        arr[i] = '~'

        if arr[0] == '~' and (len(arr) > 1 and arr[1] == '('):
            arr[0] = '-'
            return "0" + "".join(arr)
        else:
            return "".join(arr)

    def prepare(self, expression):
        """
        准备中缀表达式以便转换为后缀表示法
        :param expression: 字符串，要准备的中缀表达式
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.prepare("2+3*4")
        expression_calculator.postfix_stack = ['2', '3', '4', '*', '+']
        """
        # Implementation of the prepare method
        operator_stack = deque()
        i = 0
        while i < len(expression):
            token = expression[i]
            if token.isdigit() or (token == '~' and (i + 1 < len(expression) and expression[i + 1].isdigit())):
                num = token
                i += 1
                while i < len(expression) and expression[i].isdigit():
                    num += expression[i]
                    i += 1
                self.postfix_stack.append(num)
            elif token in {'+', '-', '*', '\/', '%', '(', ')'}:
                if token == '(':
                    operator_stack.append(token)
                elif token == ')':
                    while operator_stack and operator_stack[-1] != '(':
                        self.postfix_stack.append(operator_stack.pop())
                    operator_stack.pop()  # pop the '('
                else:
                    while (operator_stack and self.compare(token, operator_stack[-1])):
                        self.postfix_stack.append(operator_stack.pop())
                    operator_stack.append(token)
                i += 1
            else:
                i += 1

        while operator_stack:
            self.postfix_stack.append(operator_stack.pop())