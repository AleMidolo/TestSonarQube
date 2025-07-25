def is_fill_request_seq(seq):
    """
    जाँच करें कि *seq* को FillRequestSeq में बदला जा सकता है।  

    यह True तभी लौटाएगा जब:  
    - यह एक FillRequest तत्व हो,  
    - या इसमें कम से कम एक FillRequest तत्व हो,  
    - और यह Source अनुक्रम (Source sequence) न हो।
    """
    # Assuming FillRequest is a specific type or class
    is_fill_request = any(isinstance(item, FillRequest) for item in seq)
    is_source_sequence = isinstance(seq, SourceSequence)

    return is_fill_request and not is_source_sequence