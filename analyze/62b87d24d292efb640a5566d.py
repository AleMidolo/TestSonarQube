def plus_or_dot(pieces):
    """
    Restituisci un "+" se non è già presente, altrimenti restituisci un "."
    """
    if "+" not in pieces:
        return "+"
    else:
        return "."