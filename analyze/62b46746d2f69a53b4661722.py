def absorb(self, args):
    result = []
    for arg in args:
        absorbed = False
        
        # Check each pair of expressions
        for other in args:
            if arg == other:
                continue
                
            # Absorption cases
            if isinstance(other, Or) and arg in other.args:
                absorbed = True
                result.append(arg)
                break
                
            if isinstance(other, And) and arg in other.args:
                absorbed = True
                result.append(arg)
                break
                
            # Negative absorption cases
            if isinstance(other, Or) and isinstance(other.args[0], Not):
                if arg == ~other.args[0].args[0]:
                    absorbed = True
                    result.append(arg & other.args[1])
                    break
                    
            if isinstance(other, And) and isinstance(other.args[0], Not):
                if arg == ~other.args[0].args[0]:
                    absorbed = True
                    result.append(arg | other.args[1])
                    break
                    
        if not absorbed:
            result.append(arg)
            
    return result