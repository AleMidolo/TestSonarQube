def absorb(self, args):
    result = []
    for arg in args:
        # Check if arg is an AND or OR operation
        if isinstance(arg, (And, Or)):
            # Get operator and operands
            op = type(arg)
            terms = arg.args
            
            # Check each term for absorption
            absorbed = False
            for term in terms:
                # Check for regular absorption
                if term in args:
                    if (op is And and any(isinstance(t, Or) and term in t.args for t in terms)) or \
                       (op is Or and any(isinstance(t, And) and term in t.args for t in terms)):
                        result.append(term)
                        absorbed = True
                        break
                
                # Check for negative absorption
                if isinstance(term, Not):
                    neg_term = term.args[0]
                    if neg_term in args:
                        if op is And:
                            # A & (~A | B) = A & B
                            for t in terms:
                                if isinstance(t, Or) and neg_term in t.args:
                                    new_terms = [x for x in t.args if x != neg_term]
                                    result.append(And(neg_term, *new_terms))
                                    absorbed = True
                                    break
                        else:
                            # A | (~A & B) = A | B
                            for t in terms:
                                if isinstance(t, And) and neg_term in t.args:
                                    new_terms = [x for x in t.args if x != neg_term]
                                    result.append(Or(neg_term, *new_terms))
                                    absorbed = True
                                    break
            
            # If no absorption occurred, keep original term
            if not absorbed:
                result.append(arg)
        else:
            result.append(arg)
            
    return result