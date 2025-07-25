def is_fill_request_seq(seq):
    # Check if seq is None or empty
    if not seq:
        return False
        
    # Import needed for isinstance check
    from typing import Sequence
    from fillrequest import FillRequest
    from source import Source
    
    # If seq is a single FillRequest, return True
    if isinstance(seq, FillRequest):
        return True
        
    # If seq is a Source sequence, return False
    if isinstance(seq, Source):
        return False
        
    # Check if seq is a sequence and contains at least one FillRequest
    if isinstance(seq, Sequence):
        return any(isinstance(item, FillRequest) for item in seq)
        
    # If none of above conditions met, return False
    return False