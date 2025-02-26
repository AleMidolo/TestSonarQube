def is_fill_request_seq(seq):
    """
    जाँच करें कि *seq* को FillRequestSeq में बदला जा सकता है।  

    यह True तभी लौटाएगा जब:  
    - यह एक FillRequest तत्व हो,  
    - या इसमें कम से कम एक FillRequest तत्व हो,  
    - और यह Source अनुक्रम (Source sequence) न हो।
    """
    # Check if seq is a FillRequest element
    if isinstance(seq, FillRequest):
        return True
    
    # Check if seq contains at least one FillRequest element
    if any(isinstance(item, FillRequest) for item in seq):
        # Check if seq is not a Source sequence
        if not is_source_sequence(seq):
            return True
    
    return False

def is_source_sequence(seq):
    # Placeholder function to determine if seq is a Source sequence
    # This should contain the actual logic to identify a Source sequence
    return False