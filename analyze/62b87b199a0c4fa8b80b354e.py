def is_fill_request_seq(seq):
    """
    Test whether *seq* can be converted to a FillRequestSeq.

    True only if it is a FillRequest element
    or contains at least one such,
    and it is not a Source sequence.
    """
    # Assuming FillRequest and Source are classes or types that can be checked
    # Here, we assume that FillRequest and Source are types or have a specific attribute/method to identify them
    # For example, let's assume FillRequest has a method `is_fill_request()` and Source has `is_source()`
    
    # Check if the sequence itself is a FillRequest
    if hasattr(seq, 'is_fill_request') and seq.is_fill_request():
        return True
    
    # Check if the sequence contains at least one FillRequest element
    if isinstance(seq, (list, tuple)):
        for item in seq:
            if hasattr(item, 'is_fill_request') and item.is_fill_request():
                return True
    
    # Check if the sequence is a Source sequence
    if hasattr(seq, 'is_source') and seq.is_source():
        return False
    
    # If none of the above conditions are met, return False
    return False