def _get_seq_with_type(seq, bufsize=None):
    """
    Devuelve un par (secuencia, tipo).
    La secuencia se deriva de *seq*
    (o es *seq*, si este es de un tipo de secuencia).
    """
    if isinstance(seq, (str, bytes, bytearray)):
        return seq, type(seq)
    try:
        return list(seq), type(seq)
    except TypeError:
        return seq, type(seq)