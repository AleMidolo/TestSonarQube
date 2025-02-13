def is_fill_request_seq(seq):
    if not isinstance(seq, list):
        return False
    if any(isinstance(item, FillRequest) for item in seq):
        return True
    return False