def _get_seq_with_type(seq, bufsize=None):
    """
    Devuelve un par (secuencia, tipo).
    La secuencia se deriva de *seq*
    (o es *seq*, si este es de un tipo de secuencia).
    """
    # Check if seq is already a sequence type
    if isinstance(seq, (list, tuple, bytes, bytearray)):
        return seq, type(seq)
    
    # Convert iterables to list
    if hasattr(seq, '__iter__'):
        if bufsize is None:
            return list(seq), list
        else:
            # If bufsize specified, only take that many items
            return list(itertools.islice(seq, bufsize)), list
            
    # Convert single items to single-item list
    return [seq], list