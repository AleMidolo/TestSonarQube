def is_fill_request_seq(seq):
    """
    Test whether *seq* can be converted to a FillRequestSeq.

    True only if it is a FillRequest element
    or contains at least one such,
    and it is not a Source sequence.
    """
    # Import needed for type checking
    from typing import Sequence
    from collections.abc import Sequence as SequenceType
    
    # Check if seq is a Source sequence
    if hasattr(seq, 'is_source') and seq.is_source:
        return False
        
    # Check if seq itself is a FillRequest
    if hasattr(seq, 'is_fill_request') and seq.is_fill_request:
        return True
        
    # Check if seq is a sequence type
    if isinstance(seq, SequenceType):
        # Recursively check elements
        for element in seq:
            if is_fill_request_seq(element):
                return True
                
    return False