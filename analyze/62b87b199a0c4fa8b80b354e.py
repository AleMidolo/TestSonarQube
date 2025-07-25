def is_fill_request_seq(seq):
    # Import required types
    from typing import Sequence
    from fillrequest import FillRequest
    from source import Source
    
    # Check if seq is a single FillRequest
    if isinstance(seq, FillRequest):
        return True
        
    # Check if seq is a Source sequence
    if isinstance(seq, Source):
        return False
        
    # Check if seq is a sequence
    if not isinstance(seq, Sequence):
        return False
        
    # Check if sequence contains at least one FillRequest
    has_fill_request = False
    for item in seq:
        if isinstance(item, FillRequest):
            has_fill_request = True
            break
            
    return has_fill_request