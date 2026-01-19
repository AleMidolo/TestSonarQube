def calculate(self, expression):
    """
    दिए गए पोस्टफ़िक्स एक्सप्रेशन का रिज़ल्ट कैलकुलेट करें।

    :param expression: string, कैलकुलेट करने के लिए पोस्टफ़िक्स एक्सप्रेशन
    :return: float, कैलकुलेट किया गया रिज़ल्ट

    >>> expression_calculator = ExpressionCalculator()
    >>> expression_calculator.calculate("2 + 3 * 4")
    14.0
    """
    # This appears to be an infix expression based on the example, not postfix
    # Convert infix to postfix first, then evaluate
    
    def precedence(op):
        if op in ['+', '-']:
            return 1
        if op in ['*', '/']:
            return 2
        return 0
    
    def infix_to_postfix(expr):
        stack = []
        output = []
        tokens = expr.replace('(', ' ( ').replace(')', ' ) ').split()
        
        for token in tokens:
            if token.replace('.', '').replace('-', '').isdigit():
                output.append(token)
            elif token == '(':
                stack.append(token)
            elif token == ')':
                while stack and stack[-1] != '(':
                    output.append(stack.pop())
                if stack:
                    stack.pop()
            elif token in ['+', '-', '*', '/']:
                while stack and stack[-1] != '(' and precedence(stack[-1]) >= precedence(token):
                    output.append(stack.pop())
                stack.append(token)
        
        while stack:
            output.append(stack.pop())
        
        return output
    
    def evaluate_postfix(postfix):
        stack = []
        
        for token in postfix:
            if token in ['+', '-', '*', '/']:
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
            else:
                stack.append(float(token))
        
        return stack[0]
    
    postfix = infix_to_postfix(expression)
    return evaluate_postfix(postfix)