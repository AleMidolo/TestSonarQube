def calculate(self, expression):
    """
    计算给定后缀表达式的结果
    :param expression: 字符串，要计算的后缀表达式
    :return: 浮点数，计算结果
    >>> expression_calculator = ExpressionCalculator()
    >>> expression_calculator.calculate("2 + 3 * 4")
    14.0

    """
    # First, convert infix to postfix notation
    def infix_to_postfix(expr):
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        output = []
        operator_stack = []
        
        tokens = []
        i = 0
        while i < len(expr):
            if expr[i].isspace():
                i += 1
                continue
            elif expr[i].isdigit() or expr[i] == '.':
                j = i
                while j < len(expr) and (expr[j].isdigit() or expr[j] == '.'):
                    j += 1
                tokens.append(expr[i:j])
                i = j
            else:
                tokens.append(expr[i])
                i += 1
        
        for token in tokens:
            if token[0].isdigit() or (len(token) > 1 and token[0] == '.' and token[1].isdigit()):
                output.append(token)
            elif token == '(':
                operator_stack.append(token)
            elif token == ')':
                while operator_stack and operator_stack[-1] != '(':
                    output.append(operator_stack.pop())
                if operator_stack:
                    operator_stack.pop()
            elif token in precedence:
                while (operator_stack and 
                       operator_stack[-1] != '(' and 
                       operator_stack[-1] in precedence and
                       precedence[operator_stack[-1]] >= precedence[token]):
                    output.append(operator_stack.pop())
                operator_stack.append(token)
        
        while operator_stack:
            output.append(operator_stack.pop())
        
        return output
    
    # Evaluate postfix expression
    def evaluate_postfix(postfix):
        stack = []
        
        for token in postfix:
            if token not in ['+', '-', '*', '/', '^']:
                stack.append(float(token))
            else:
                if len(stack) < 2:
                    raise ValueError("Invalid expression")
                b = stack.pop()
                a = stack.pop()
                
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                    stack.append(a / b)
                elif token == '^':
                    stack.append(a ** b)
        
        return stack[0] if stack else 0.0
    
    postfix = infix_to_postfix(expression)
    return evaluate_postfix(postfix)