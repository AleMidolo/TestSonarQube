def is_fill_request_seq(seq):
    """
    Test whether *seq* can be converted to a FillRequestSeq.

    True only if it is a FillRequest element
    or contains at least one such,
    and it is not a Source sequence.
    """
    if not seq:
        return False
    
    is_fill_request = any(isinstance(item, FillRequest) for item in seq)
    is_source_sequence = isinstance(seq, SourceSequence)

    return is_fill_request and not is_source_sequence