def is_fill_request_seq(seq):
    from collections.abc import Sequence
    from typing import Union
    
    # Check if seq is a FillRequest object
    try:
        if isinstance(seq, FillRequest):
            return True
    except NameError:
        pass
        
    # Check if seq is a Source sequence
    try:
        if isinstance(seq, Source):
            return False
    except NameError:
        pass
        
    # Check if seq is a sequence containing at least one FillRequest
    if isinstance(seq, Sequence):
        try:
            return any(isinstance(item, FillRequest) for item in seq)
        except NameError:
            return False
            
    return False