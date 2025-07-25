def absorb(self, args):
    # Create copy of input list to avoid modifying original
    result = args.copy()
    
    # Keep track if any changes were made in a pass
    changed = True
    while changed:
        changed = False
        
        # Check each pair of expressions
        for i in range(len(result)):
            for j in range(len(result)):
                if i == j:
                    continue
                    
                # Get expressions to compare
                expr1 = result[i]
                expr2 = result[j]
                
                # Check absorption cases
                # A & (A | B) = A
                if expr1.is_and() and expr2.is_or():
                    if expr1 in expr2.args:
                        result[j] = expr1
                        changed = True
                        
                # A | (A & B) = A        
                elif expr1.is_or() and expr2.is_and():
                    if expr1 in expr2.args:
                        result[j] = expr1
                        changed = True
                
                # Check negative absorption cases
                # A & (~A | B) = A & B
                if expr1.is_and() and expr2.is_or():
                    if expr1.negate() in expr2.args:
                        new_expr = expr1 & expr2.args[1]
                        result[j] = new_expr
                        changed = True
                        
                # A | (~A & B) = A | B
                elif expr1.is_or() and expr2.is_and():
                    if expr1.negate() in expr2.args:
                        new_expr = expr1 | expr2.args[1]
                        result[j] = new_expr
                        changed = True
                        
        # Remove any duplicates
        result = list(set(result))
                        
    return result