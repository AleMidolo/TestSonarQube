def _get_seq_with_type(seq, bufsize=None):
    """
    Restituisce una coppia (sequenza, tipo).  
    La sequenza è derivata da *seq*  
    (oppure è *seq*, se quest'ultima è di un tipo sequenza).
    """
    if isinstance(seq, (list, tuple, set, str)):
        return seq, type(seq)
    else:
        if bufsize is not None:
            seq = list(seq)[:bufsize]
        else:
            seq = list(seq)
        return seq, type(seq)