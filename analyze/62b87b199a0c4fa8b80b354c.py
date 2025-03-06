def _get_seq_with_type(seq, bufsize=None):
    """
    (sequence, type) जोड़ी लौटाता है।
    Sequence *seq* से प्राप्त किया जाता है
    (या *seq* ही होता है, यदि वह sequence प्रकार का है)।
    """
    if isinstance(seq, (list, tuple, str, bytes)):
        return seq, type(seq)
    else:
        return list(seq), type(seq)