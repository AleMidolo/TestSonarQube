def absorb(self, args):
    """
    Dato un insieme `args` di espressioni, restituisce una nuova lista di espressioni applicando l'assorbimento e l'assorbimento negativo.

    Consulta https://en.wikipedia.org/wiki/Absorption_law

    Assorbimento::

        A & (A | B) = A, A | (A & B) = A

    Assorbimento negativo::

        A & (~A | B) = A & B, A | (~A & B) = A | B
    """
    def absorb_expression(expr):
        # Implement absorption laws
        if isinstance(expr, tuple) and len(expr) == 3:
            op1, operator, op2 = expr
            if operator == '&':
                if op1 == op2:
                    return op1
                elif isinstance(op2, tuple) and op2[0] == op1 and op2[1] == '|':
                    return op1
                elif isinstance(op2, tuple) and op2[0] == '~' and op2[1] == op1:
                    return (op1, '&', op2[2])
            elif operator == '|':
                if op1 == op2:
                    return op1
                elif isinstance(op2, tuple) and op2[0] == op1 and op2[1] == '&':
                    return op1
                elif isinstance(op2, tuple) and op2[0] == '~' and op2[1] == op1:
                    return (op1, '|', op2[2])
        return expr

    return [absorb_expression(expr) for expr in args]