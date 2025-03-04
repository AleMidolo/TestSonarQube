def absorb(self, args):
    result = []
    for arg in args:
        # Check if arg is an AND or OR operation
        if isinstance(arg, (And, Or)):
            op = arg.op
            terms = arg.args
            
            # Look for absorption patterns in each term
            absorbed = False
            for i, term1 in enumerate(terms):
                for j, term2 in enumerate(terms):
                    if i == j:
                        continue
                        
                    # Regular absorption: A & (A | B) = A or A | (A & B) = A
                    if (op == '&' and isinstance(term2, Or) and term1 in term2.args) or \
                       (op == '|' and isinstance(term2, And) and term1 in term2.args):
                        result.append(term1)
                        absorbed = True
                        break
                        
                    # Negative absorption: A & (~A | B) = A & B or A | (~A & B) = A | B
                    if op == '&' and isinstance(term2, Or):
                        for t in term2.args:
                            if isinstance(t, Not) and t.arg == term1:
                                remaining = [x for x in term2.args if x != t]
                                result.append(And(term1, *remaining))
                                absorbed = True
                                break
                    elif op == '|' and isinstance(term2, And):
                        for t in term2.args:
                            if isinstance(t, Not) and t.arg == term1:
                                remaining = [x for x in term2.args if x != t]
                                result.append(Or(term1, *remaining))
                                absorbed = True
                                break
                                
                if absorbed:
                    break
                    
            # If no absorption found, keep original expression
            if not absorbed:
                result.append(arg)
        else:
            # Not an operation, keep as is
            result.append(arg)
            
    return result