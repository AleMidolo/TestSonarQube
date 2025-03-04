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
                if (expr1.op == '&' and 
                    expr2.op == '|' and
                    expr1.left in [expr2.left, expr2.right]):
                    result[j] = expr1
                    changed = True
                    
                # A | (A & B) = A 
                elif (expr1.op == '|' and
                      expr2.op == '&' and 
                      expr1.left in [expr2.left, expr2.right]):
                    result[j] = expr1
                    changed = True
                    
                # Check negative absorption
                # A & (~A | B) = A & B
                elif (expr1.op == '&' and
                      expr2.op == '|' and
                      expr2.left.op == '~' and
                      expr2.left.expr == expr1.left):
                    result[j] = expr1 & expr2.right
                    changed = True
                    
                # A | (~A & B) = A | B
                elif (expr1.op == '|' and
                      expr2.op == '&' and
                      expr2.left.op == '~' and
                      expr2.left.expr == expr1.left):
                    result[j] = expr1 | expr2.right
                    changed = True
                    
    # Remove duplicates while preserving order
    seen = set()
    return [x for x in result if not (x in seen or seen.add(x))]