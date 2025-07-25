def _get_seq_with_type(seq, bufsize=None):
    """
    (sequence, type) जोड़ी लौटाता है।
    Sequence *seq* से प्राप्त किया जाता है
    (या *seq* ही होता है, यदि वह sequence प्रकार का है)।
    """
    if isinstance(seq, (list, tuple, range)):
        return seq, type(seq)
    elif isinstance(seq, str):
        return list(seq), list
    elif hasattr(seq, '__iter__'):
        # Convert iterator to list with optional buffer size
        if bufsize is not None:
            return list(itertools.islice(seq, bufsize)), list
        return list(seq), list
    else:
        # If not a sequence, wrap in list
        return [seq], list