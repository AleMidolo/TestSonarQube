def is_fill_request_seq(seq):
    from collections.abc import Sequence
    from typing import Union
    
    # Helper function to check if an item is a FillRequest
    def is_fill_request(item):
        # Assuming FillRequest is a class/type that represents fill requests
        try:
            return isinstance(item, FillRequest)
        except NameError:
            return False
            
    # Check if seq is None
    if seq is None:
        return False
        
    # Check if seq is a Source sequence
    try:
        if isinstance(seq, Source):
            return False
    except NameError:
        pass
        
    # Handle single item case
    if not isinstance(seq, Sequence):
        return is_fill_request(seq)
        
    # Check if sequence contains at least one FillRequest
    return any(is_fill_request(item) for item in seq)