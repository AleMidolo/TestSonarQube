def _get_seq_with_type(seq, bufsize=None):
    """
    Devuelve un par (secuencia, tipo).
    La secuencia se deriva de *seq*
    (o es *seq*, si este es de un tipo de secuencia).
    """
    # Check if seq is already a sequence type
    if isinstance(seq, (list, tuple, set, frozenset)):
        return seq, type(seq)
    
    # Convert iterables to list
    if hasattr(seq, '__iter__'):
        # Use bufsize if provided, otherwise convert entire sequence
        if bufsize is not None:
            return list(itertools.islice(seq, bufsize)), list
        return list(seq), list
        
    # If not iterable, wrap in list
    return [seq], list