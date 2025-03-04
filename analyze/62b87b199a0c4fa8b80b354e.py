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
        
    # Import needed for isinstance check
    from typing import Sequence
    from fill_request import FillRequest, Source
    
    # If seq is a single FillRequest and not a Source
    if isinstance(seq, FillRequest) and not isinstance(seq, Source):
        return True
        
    # If seq is a sequence, check if it contains at least one FillRequest
    if isinstance(seq, Sequence):
        # Return False if it's a Source sequence
        if isinstance(seq, Source):
            return False
            
        # Check each element
        for element in seq:
            if isinstance(element, FillRequest):
                return True
                
    return False