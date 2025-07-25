def is_fill_request_seq(seq):
    """
    Test whether *seq* can be converted to a FillRequestSeq.

    True only if it is a FillRequest element
    or contains at least one such,
    and it is not a Source sequence.
    """
    # Assuming FillRequest and Source are classes or types that can be checked
    # For example, let's assume FillRequest is a class and Source is another class
    # You would need to replace these with the actual checks based on your context
    
    # Check if seq is a FillRequest element
    if isinstance(seq, FillRequest):
        return True
    
    # Check if seq contains at least one FillRequest element
    if hasattr(seq, '__iter__'):
        for item in seq:
            if isinstance(item, FillRequest):
                return True
    
    # Check if seq is not a Source sequence
    if isinstance(seq, Source):
        return False
    
    # If none of the above conditions are met, return False
    return False