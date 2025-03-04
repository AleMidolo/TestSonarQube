def _get_seq_with_type(seq, bufsize=None):
    """
    Restituisce una coppia (sequenza, tipo).  
    La sequenza è derivata da *seq*  
    (oppure è *seq*, se quest'ultima è di un tipo sequenza).
    """
    # Check if seq is already a sequence type
    if isinstance(seq, (list, tuple, bytes, bytearray)):
        return seq, type(seq)
    
    # Convert to bytes if it's a string
    if isinstance(seq, str):
        return seq.encode(), bytes
        
    # Try to convert to sequence if it's an iterator/generator
    try:
        if bufsize is not None:
            seq_list = list(seq)[:bufsize]
        else:
            seq_list = list(seq)
        return seq_list, list
    except:
        raise TypeError(f"Cannot convert {type(seq)} to sequence")