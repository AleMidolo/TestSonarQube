def is_fill_request_seq(seq):
    from collections.abc import Sequence
    from typing import Union
    
    # Helper function to check if an item is a FillRequest
    def is_fill_request(item):
        # Assuming FillRequest is a class/type that exists in the codebase
        try:
            return isinstance(item, FillRequest)
        except NameError:
            return False
            
    # Check if seq is a Source sequence
    try:
        if isinstance(seq, Source):
            return False
    except NameError:
        pass
        
    # If seq is a single item, check if it's a FillRequest
    if not isinstance(seq, Sequence):
        return is_fill_request(seq)
        
    # If seq is a sequence, check if it contains at least one FillRequest
    has_fill_request = False
    for item in seq:
        if is_fill_request(item):
            has_fill_request = True
            break
            
    return has_fill_request