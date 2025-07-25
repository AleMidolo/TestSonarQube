def is_fill_request_seq(seq):
    """
    Test whether *seq* can be converted to a FillRequestSeq.

    True only if it is a FillRequest element
    or contains at least one such,
    and it is not a Source sequence.
    """
    # Check if seq is a Source sequence
    if hasattr(seq, 'is_source') and seq.is_source:
        return False
        
    # Check if seq itself is a FillRequest
    if hasattr(seq, 'is_fill_request') and seq.is_fill_request:
        return True
        
    # Check if seq is iterable and contains a FillRequest
    try:
        return any(hasattr(item, 'is_fill_request') and item.is_fill_request 
                  for item in seq)
    except TypeError:
        return False