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
    
    # Check if seq is a single FillRequest element
    if hasattr(seq, 'is_fill_request') and seq.is_fill_request:
        return True
        
    # Check if seq is a Source sequence - return False if so
    if hasattr(seq, 'is_source') and seq.is_source:
        return False
        
    # Check if seq is a sequence type
    if not isinstance(seq, SequenceType):
        return False
        
    # Check if any element in sequence is a FillRequest
    for element in seq:
        if hasattr(element, 'is_fill_request') and element.is_fill_request:
            return True
            
    return False