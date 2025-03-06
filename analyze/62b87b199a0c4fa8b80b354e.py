def is_fill_request_seq(seq):
    """
    Verifica se *seq* può essere convertito in un oggetto di tipo FillRequestSeq.

    Restituisce `True` solo se *seq* è un elemento di tipo FillRequest  
    o contiene almeno un elemento di questo tipo,  
    e non è una sequenza di tipo Source.
    """
    # Assuming FillRequest and Source are defined somewhere
    from typing import Sequence, Any

    def is_fill_request(item: Any) -> bool:
        # Placeholder for the actual check
        return isinstance(item, FillRequest)

    def is_source(item: Any) -> bool:
        # Placeholder for the actual check
        return isinstance(item, Source)

    if isinstance(seq, Sequence):
        # Check if any element in the sequence is a FillRequest
        has_fill_request = any(is_fill_request(item) for item in seq)
        # Check if the sequence is not a Source sequence
        is_not_source_seq = not all(is_source(item) for item in seq)
        return has_fill_request and is_not_source_seq
    else:
        # If it's not a sequence, check if it's a FillRequest
        return is_fill_request(seq) and not is_source(seq)