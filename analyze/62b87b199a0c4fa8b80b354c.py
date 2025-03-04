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
        # Convert other iterables to list
        if bufsize is None:
            return list(seq), list
        else:
            # Use bufsize if specified
            return list(itertools.islice(seq, bufsize)), list
    else:
        # If not iterable, wrap in list
        return [seq], list