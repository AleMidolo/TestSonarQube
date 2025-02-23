def absorb(self, args):
    """
    Dada una secuencia `args` de expresiones, devuelve una nueva lista de expresiones aplicando absorción y absorción negativa.

    Consulta https://es.wikipedia.org/wiki/Leyes_de_absorci%C3%B3n

    Absorción::

        A & (A | B) = A, A | (A & B) = A

    Absorción negativa::

        A & (~A | B) = A & B, A | (~A & B) = A | B
    """
    result = []
    for expr in args:
        if isinstance(expr, tuple) and len(expr) == 3:
            a, op, b = expr
            if op == '&':
                if (a == b) or (b == ('~', a)):
                    result.append(a)
                elif isinstance(b, tuple) and b[0] == '|':
                    if a == b[1]:
                        result.append(a)
                    elif b[1] == ('~', a):
                        result.append((a, '&', b[2]))
                    else:
                        result.append(expr)
                else:
                    result.append(expr)
            elif op == '|':
                if (a == b) or (b == ('~', a)):
                    result.append(a)
                elif isinstance(b, tuple) and b[0] == '&':
                    if a == b[1]:
                        result.append(a)
                    elif b[1] == ('~', a):
                        result.append((a, '|', b[2]))
                    else:
                        result.append(expr)
                else:
                    result.append(expr)
        else:
            result.append(expr)
    return result