def _get_seq_with_type(seq, bufsize=None):
    """
    Devuelve un par (secuencia, tipo).
    La secuencia se deriva de *seq*
    (o es *seq*, si este es de un tipo de secuencia).
    """
    if isinstance(seq, (str, bytes, bytearray)):
        return seq, type(seq)
    if hasattr(seq, '__iter__') and not isinstance(seq, (list, tuple)):
        seq = list(seq)
    return seq, type(seq)