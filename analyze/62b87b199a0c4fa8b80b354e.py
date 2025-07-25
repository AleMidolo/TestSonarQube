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
        
    # Import needed types if not already imported
    from typing import Sequence
    from .fill_request import FillRequest
    from .source import Source
    
    # If seq is a single element, check if it's a FillRequest
    if isinstance(seq, FillRequest):
        return True
        
    # If seq is a Source sequence, return False
    if isinstance(seq, Source):
        return False
        
    # If seq is a sequence, check if it contains at least one FillRequest
    if isinstance(seq, Sequence):
        return any(isinstance(item, FillRequest) for item in seq)
        
    # If none of the above conditions are met, return False
    return False