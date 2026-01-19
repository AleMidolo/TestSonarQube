def calculate(self, expression):
    """
    दिए गए पोस्टफ़िक्स एक्सप्रेशन का रिज़ल्ट कैलकुलेट करें।

    :param expression: string, कैलकुलेट करने के लिए पोस्टफ़िक्स एक्सप्रेशन
    :return: float, कैलकुलेट किया गया रिज़ल्ट

    >>> expression_calculator = ExpressionCalculator()
    >>> expression_calculator.calculate("2 + 3 * 4")
    14.0
    """
    # Convert infix to postfix first, then evaluate
    def precedence(op):
        if op in ['+', '-']:
            return 1
        if op in ['*', '/']:
            return 2
        return 0
    
    def infix_to_postfix(expr):
        stack = []
        postfix = []
        tokens = expr.replace('(', ' ( ').replace(')', ' ) ').split()
        
        for token in tokens:
            if token.replace('.', '').replace('-', '').isdigit():
                postfix.append(float(token))
            elif token == '(':
                stack.append(token)
            elif token == ')':
                while stack and stack[-1] != '(':
                    postfix.append(stack.pop())
                stack.pop()  # Remove '('
            elif token in ['+', '-', '*', '/']:
                while stack and stack[-1] != '(' and precedence(stack[-1]) >= precedence(token):
                    postfix.append(stack.pop())
                stack.append(token)
        
        while stack:
            postfix.append(stack.pop())
        
        return postfix
    
    def evaluate_postfix(postfix):
        stack = []
        
        for token in postfix:
            if isinstance(token, float):
                stack.append(token)
            else:
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
        
        return stack[0]
    
    postfix = infix_to_postfix(expression)
    return evaluate_postfix(postfix)