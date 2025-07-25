def absorb(self, args):
    result = list(args)
    changed = True
    
    while changed:
        changed = False
        n = len(result)
        
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                    
                # Assorbimento A & (A | B) = A
                if (isinstance(result[i], And) and 
                    isinstance(result[j], Or) and
                    result[i].args[0] in result[j].args):
                    result[j] = result[i]
                    changed = True
                
                # Assorbimento A | (A & B) = A 
                if (isinstance(result[i], Or) and
                    isinstance(result[j], And) and 
                    result[i].args[0] in result[j].args):
                    result[j] = result[i]
                    changed = True
                    
                # Assorbimento negativo A & (~A | B) = A & B
                if (isinstance(result[i], And) and
                    isinstance(result[j], Or) and
                    Not(result[i].args[0]) in result[j].args):
                    new_args = [arg for arg in result[j].args 
                              if arg != Not(result[i].args[0])]
                    result[j] = And(result[i].args[0], *new_args)
                    changed = True
                
                # Assorbimento negativo A | (~A & B) = A | B
                if (isinstance(result[i], Or) and
                    isinstance(result[j], And) and
                    Not(result[i].args[0]) in result[j].args):
                    new_args = [arg for arg in result[j].args
                              if arg != Not(result[i].args[0])]
                    result[j] = Or(result[i].args[0], *new_args)
                    changed = True
                    
    return result