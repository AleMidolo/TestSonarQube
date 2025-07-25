def is_fill_request_seq(seq):
    """
    Test whether *seq* can be converted to a FillRequestSeq.

    True only if it is a FillRequest element
    or contains at least one such,
    and it is not a Source sequence.
    """
    # Check if seq is None or empty
    if not seq:
        return False
        
    # Import needed for isinstance checks
    from collections.abc import Sequence
    
    # If seq is a single element, check if it's a FillRequest
    if not isinstance(seq, Sequence):
        return isinstance(seq, FillRequest)
        
    # Check if it's a Source sequence
    if isinstance(seq, Source):
        return False
        
    # Check if any element is a FillRequest
    return any(isinstance(item, FillRequest) for item in seq)