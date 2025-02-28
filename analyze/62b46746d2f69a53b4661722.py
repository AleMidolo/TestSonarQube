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
    if not args:
        return []

    new_args = []
    for expr in args:
        if isinstance(expr, tuple):
            if len(expr) == 3:
                op, left, right = expr
                if op == '&':
                    if left == right:
                        new_args.append(left)
                    elif isinstance(right, tuple) and len(right) == 3:
                        r_op, r_left, r_right = right
                        if r_op == '|' and r_left == left:
                            new_args.append(left)
                        elif r_op == '|' and r_left == ('~', left):
                            new_args.append((op, left, r_right))
                elif op == '|':
                    if left == right:
                        new_args.append(left)
                    elif isinstance(right, tuple) and len(right) == 3:
                        r_op, r_left, r_right = right
                        if r_op == '&' and r_left == left:
                            new_args.append(left)
                        elif r_op == '&' and r_left == ('~', left):
                            new_args.append((op, left, r_right))
            else:
                new_args.append(expr)
        else:
            new_args.append(expr)
    
    return new_args