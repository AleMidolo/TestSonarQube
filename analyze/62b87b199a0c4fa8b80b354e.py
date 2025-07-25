def is_fill_request_seq(seq):
    """
    जाँच करें कि *seq* को FillRequestSeq में बदला जा सकता है।  

    यह True तभी लौटाएगा जब:  
    - यह एक FillRequest तत्व हो,  
    - या इसमें कम से कम एक FillRequest तत्व हो,  
    - और यह Source अनुक्रम (Source sequence) न हो।
    """
    # Assuming FillRequest is a class or type that represents a FillRequest element
    # Assuming Source sequence is a specific type or class that represents a Source sequence
    
    # Check if seq is a single FillRequest element
    if isinstance(seq, FillRequest):
        return True
    
    # Check if seq is a sequence and contains at least one FillRequest element
    if isinstance(seq, (list, tuple)) and any(isinstance(item, FillRequest) for item in seq):
        # Check if seq is not a Source sequence
        if not isinstance(seq, SourceSequence):
            return True
    
    return False