def is_fill_request_seq(seq):
    """
    जाँच करें कि *seq* को FillRequestSeq में बदला जा सकता है।  

    यह True तभी लौटाएगा जब:  
    - यह एक FillRequest तत्व हो,  
    - या इसमें कम से कम एक FillRequest तत्व हो,  
    - और यह Source अनुक्रम (Source sequence) न हो।
    """
    # Assuming FillRequest is a class or type that represents a FillRequest element
    # and SourceSequence is a class or type that represents a Source sequence.
    # You need to replace these with the actual types or classes used in your code.
    
    from typing import Sequence
    
    def is_fill_request(element):
        # Replace with actual check for FillRequest
        return isinstance(element, FillRequest)
    
    def is_source_sequence(seq):
        # Replace with actual check for SourceSequence
        return isinstance(seq, SourceSequence)
    
    if is_source_sequence(seq):
        return False
    
    if is_fill_request(seq):
        return True
    
    if isinstance(seq, Sequence):
        return any(is_fill_request(element) for element in seq)
    
    return False