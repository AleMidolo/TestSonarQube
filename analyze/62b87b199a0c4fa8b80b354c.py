def _get_seq_with_type(seq, bufsize=None):
    """
    Devuelve un par (secuencia, tipo).
    La secuencia se deriva de *seq*
    (o es *seq*, si este es de un tipo de secuencia).
    """
    if isinstance(seq, (list, tuple, str, bytes, bytearray)):
        return seq, type(seq)
    else:
        if bufsize is None:
            bufsize = 1024
        if hasattr(seq, 'read'):
            return seq.read(bufsize), type(seq)
        else:
            return list(seq), type(seq)