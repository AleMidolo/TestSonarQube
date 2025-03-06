def plus_or_dot(pezzi):
    """
    Restituisci un "+" se non è già presente, altrimenti restituisci un "."
    """
    if '+' not in pezzi:
        return '+'
    else:
        return '.'