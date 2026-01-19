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
                j = i
                while j < len(expression) and (expression[j].isdigit() or expression[j] == '.'):
                    j += 1
                num = float(expression[i:j])
                # Skip the digits we've processed
                if j > i + 1:
                    continue
            
            # Process operation when we hit an operator or reach the end
            if char in '+-*/' or i == len(expression) - 1:
                if i == len(expression) - 1 and char.isdigit():
                    # Last character is a digit, process it
                    pass
                
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
                
                # Update operation for next iteration
                if i < len(expression) - 1:
                    operation = char
                    num = 0
        
        return float(sum(stack))
    
    except:
        return None