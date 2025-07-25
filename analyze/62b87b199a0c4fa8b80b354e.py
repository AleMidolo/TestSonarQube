def is_fill_request_seq(seq):
    """
    Test whether *seq* can be converted to a FillRequestSeq.

    True only if it is a FillRequest element
    or contains at least one such,
    and it is not a Source sequence.
    """
    # Import needed for type checking
    from collections.abc import Sequence
    from typing import Any

    # Helper function to check if item is a FillRequest
    def is_fill_request(item: Any) -> bool:
        return hasattr(item, 'fill_request') and callable(item.fill_request)

    # Check if seq itself is a FillRequest
    if is_fill_request(seq):
        return True

    # Check if seq is a Source sequence (which should return False)
    if hasattr(seq, 'source'):
        return False

    # If seq is a sequence, check if it contains any FillRequests
    if isinstance(seq, Sequence):
        return any(is_fill_request(item) for item in seq)

    return False