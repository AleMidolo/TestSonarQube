def absorb(self, args):
    result = []
    for expr in args:
        if isinstance(expr, tuple) and len(expr) == 3:
            a, op, b = expr
            if op == '&':
                if b == ('|', a, _):
                    result.append(a)
                elif b == ('|', ('~', a), _):
                    result.append(('&', a, b[2]))
                else:
                    result.append(expr)
            elif op == '|':
                if b == ('&', a, _):
                    result.append(a)
                elif b == ('&', ('~', a), _):
                    result.append(('|', a, b[2]))
                else:
                    result.append(expr)
        else:
            result.append(expr)
    return result