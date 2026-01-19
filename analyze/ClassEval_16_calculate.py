def calculate(self, expression):
    """
    दिए गए एक्सप्रेशन की वैल्यू कैलकुलेट करें।

    :param expression: string, दिया गया एक्सप्रेशन
    :return: अगर सफल रहा, तो एक्सप्रेशन की वैल्यू रिटर्न करता है; नहीं तो None रिटर्न करता है

    >>> calculator = Calculator()
    >>> calculator.calculate('1+2-3')
    0.0
    """
    try:
        # Remove whitespace
        expression = expression.replace(' ', '')
        
        if not expression:
            return None
        
        # Stack to store numbers
        stack = []
        num = 0
        operation = '+'
        
        for i, char in enumerate(expression):
            if char.isdigit() or char == '.':
                # Build the number (handle multi-digit and decimal numbers)
                if char == '.':
                    # Handle decimal numbers
                    decimal_part = ''
                    j = i + 1
                    while j < len(expression) and expression[j].isdigit():
                        decimal_part += expression[j]
                        j += 1
                    num = float(str(int(num)) + '.' + decimal_part) if decimal_part else float(num)
                else:
                    num = num * 10 + int(char)
            
            # If current char is an operator or last character
            if char in '+-*/' or i == len(expression) - 1:
                if i == len(expression) - 1 and char.isdigit():
                    # Process the last number
                    pass
                
                # Apply previous operation
                if operation == '+':
                    stack.append(num)
                elif operation == '-':
                    stack.append(-num)
                elif operation == '*':
                    stack.append(stack.pop() * num)
                elif operation == '/':
                    if num == 0:
                        return None
                    stack.append(stack.pop() / num)
                
                # Update operation and reset num
                if char in '+-*/':
                    operation = char
                    num = 0
        
        return float(sum(stack))
    
    except:
        return None