def is_fill_request_seq(seq):
    # Check if seq is None or empty
    if not seq:
        return False
        
    # Import needed for isinstance check
    from typing import Sequence
    from fillrequest import FillRequest
    
    # If seq is a single FillRequest, return True
    if isinstance(seq, FillRequest):
        return True
        
    # Check if seq is a sequence and not a string (which is also a sequence)
    if not isinstance(seq, Sequence) or isinstance(seq, str):
        return False
        
    # Check if seq contains at least one FillRequest
    has_fill_request = False
    for item in seq:
        if isinstance(item, FillRequest):
            has_fill_request = True
            break
            
    # Check if seq is not a Source sequence
    from source import Source
    is_source_seq = isinstance(seq, Source) or (hasattr(seq, '__iter__') and all(isinstance(x, Source) for x in seq))
    
    # Return True if has at least one FillRequest and is not a Source sequence
    return has_fill_request and not is_source_seq