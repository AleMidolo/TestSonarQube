def is_fill_request_seq(seq):
    """
    Test whether *seq* can be converted to a FillRequestSeq.

    True only if it is a FillRequest element
    or contains at least one such,
    and it is not a Source sequence.
    """
    if not seq:
        return False
    
    # Check if the sequence is a Source sequence
    if isinstance(seq, Source):
        return False
    
    # Check if the sequence contains at least one FillRequest element
    for element in seq:
        if isinstance(element, FillRequest):
            return True
            
    return False