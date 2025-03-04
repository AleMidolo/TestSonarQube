def is_fill_request_seq(seq):
    from typing import Sequence
    from fillrequest import FillRequest
    from source import Source

    # Check if seq is a FillRequest directly
    if isinstance(seq, FillRequest):
        return True
        
    # Check if seq is a Source sequence
    if isinstance(seq, Source):
        return False
        
    # Check if seq is a sequence
    if not isinstance(seq, Sequence):
        return False
        
    # Check if sequence contains at least one FillRequest
    for item in seq:
        if isinstance(item, FillRequest):
            return True
            
    return False