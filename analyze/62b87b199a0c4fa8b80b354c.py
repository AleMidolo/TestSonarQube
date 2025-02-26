def _get_seq_with_type(seq, bufsize=None):
    """
    Return a (sequence, type) pair.
    Sequence is derived from *seq*
    (or is *seq*, if that is of a sequence type).
    """
    if isinstance(seq, (list, tuple, set, str)):
        return seq, type(seq)
    else:
        if bufsize is not None:
            seq = list(seq)[:bufsize]
        else:
            seq = list(seq)
        return seq, type(seq)