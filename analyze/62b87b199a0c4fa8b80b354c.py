def _get_seq_with_type(seq, bufsize=None):
    if isinstance(seq, (list, tuple, set)):
        return (seq, type(seq))
    else:
        return (list(seq), type(seq))