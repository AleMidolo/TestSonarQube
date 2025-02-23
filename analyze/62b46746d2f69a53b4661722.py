def absorb(self, args):
    """
    Given an `args` sequence of expressions, return a new list of expression
    applying absorption and negative absorption.

    See https://en.wikipedia.org/wiki/Absorption_law

    Absorption::

        A & (A | B) = A, A | (A & B) = A

    Negative absorption::

        A & (~A | B) = A & B, A | (~A & B) = A | B
    """
    result = []
    for expr in args:
        if isinstance(expr, tuple) and len(expr) == 3:
            op1, operator, op2 = expr
            if operator == '&':
                if op1 == op2 or (op1 == f'~{op2}' or op2 == f'~{op1}'):
                    result.append(op1)
                elif op1 == f'({op1} | {op2})':
                    result.append(op1)
                else:
                    result.append(expr)
            elif operator == '|':
                if op1 == op2 or (op1 == f'~{op2}' or op2 == f'~{op1}'):
                    result.append(op1)
                elif op1 == f'({op1} & {op2})':
                    result.append(op1)
                else:
                    result.append(expr)
        else:
            result.append(expr)
    return result