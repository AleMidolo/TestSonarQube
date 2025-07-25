def is_fill_request_seq(seq):
    """
    Test whether *seq* can be converted to a FillRequestSeq.

    True only if it is a FillRequest element
    or contains at least one such,
    and it is not a Source sequence.
    """
    # Assuming FillRequest and Source are classes or types that can be checked
    # For example, FillRequest could be a class and Source could be another class
    # This is a placeholder implementation; you would need to replace it with actual logic
    
    # Example logic:
    # Check if seq is an instance of FillRequest
    if isinstance(seq, FillRequest):
        return True
    
    # Check if seq is a sequence and contains at least one FillRequest element
    if isinstance(seq, (list, tuple)):
        return any(isinstance(item, FillRequest) for item in seq)
    
    # Check if seq is not a Source sequence
    if isinstance(seq, Source):
        return False
    
    # If none of the above conditions are met, return False
    return False