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
        
    # Handle single item case
    if not isinstance(seq, Sequence):
        return is_fill_request(seq)
        
    # Handle sequence case
    has_fill_request = False
    for item in seq:
        if is_fill_request(item):
            has_fill_request = True
            break
            
    return has_fill_request