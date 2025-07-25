def _get_seq_with_type(seq, bufsize=None):
    """
    Restituisce una coppia (sequenza, tipo).  
    La sequenza è derivata da *seq*  
    (oppure è *seq*, se quest'ultima è di un tipo sequenza).
    """
    if isinstance(seq, (str, bytes, bytearray, list, tuple)):
        return seq, type(seq)
    else:
        if bufsize is None:
            bufsize = 1024
        if hasattr(seq, 'read'):
            return seq.read(bufsize), type(seq)
        else:
            return list(seq), type(seq)