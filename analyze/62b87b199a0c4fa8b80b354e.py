def is_fill_request_seq(seq):
    """
    Test whether *seq* can be converted to a FillRequestSeq.

    True only if it is a FillRequest element
    or contains at least one such,
    and it is not a Source sequence.
    """
    # Assuming FillRequest and Source are classes or types that can be checked
    # Here, we assume that FillRequest and Source are types or have a specific attribute
    # that can be checked to determine if an element is of that type.
    
    # Check if the sequence itself is a FillRequest
    if isinstance(seq, FillRequest):
        return True
    
    # Check if the sequence contains at least one FillRequest element
    if any(isinstance(item, FillRequest) for item in seq):
        # Ensure that the sequence is not a Source sequence
        if not isinstance(seq, Source):
            return True
    
    return False