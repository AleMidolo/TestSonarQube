def plus_or_dot(pieces):
    """
    Devuelve un "+" si no tenemos uno ya, de lo contrario, devuelve un "."
    """
    if '+' not in pieces:
        return '+'
    else:
        return '.'