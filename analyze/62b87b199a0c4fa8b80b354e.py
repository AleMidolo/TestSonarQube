def is_fill_request_seq(seq):
    """
    Test whether *seq* can be converted to a FillRequestSeq.

    True only if it is a FillRequest element
    or contains at least one such,
    and it is not a Source sequence.
    """
    # Assuming FillRequest and Source are classes or types that can be checked
    # Replace with actual type checking logic as needed
    def is_fill_request(element):
        return isinstance(element, FillRequest)  # Replace FillRequest with actual type

    def is_source(element):
        return isinstance(element, Source)  # Replace Source with actual type

    if is_source(seq):
        return False

    if is_fill_request(seq):
        return True

    if isinstance(seq, (list, tuple)):
        return any(is_fill_request(element) for element in seq)

    return False