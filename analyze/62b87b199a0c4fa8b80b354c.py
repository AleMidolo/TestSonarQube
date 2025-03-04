def _get_seq_with_type(seq, bufsize=None):
    """
    Return a (sequence, type) pair.
    Sequence is derived from *seq*
    (or is *seq*, if that is of a sequence type).
    """
    # Check if seq is already a sequence type
    if isinstance(seq, (list, tuple, range)):
        return seq, type(seq)
    
    # Convert to list if not a sequence
    if hasattr(seq, '__iter__'):
        # Convert iterator to list
        seq_list = list(seq)
        return seq_list, list
    
    # If not iterable, wrap in list
    return [seq], list