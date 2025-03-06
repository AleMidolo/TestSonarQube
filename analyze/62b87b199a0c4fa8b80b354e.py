def is_fill_request_seq(seq):
    """
    Test whether *seq* can be converted to a FillRequestSeq.

    True only if it is a FillRequest element
    or contains at least one such,
    and it is not a Source sequence.
    """
    from collections.abc import Sequence

    # Assuming FillRequest and Source are defined elsewhere
    # For example:
    # class FillRequest: pass
    # class Source: pass

    if isinstance(seq, FillRequest):
        return True
    elif isinstance(seq, Sequence) and not isinstance(seq, Source):
        return any(isinstance(item, FillRequest) for item in seq)
    else:
        return False