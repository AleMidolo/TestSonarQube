def is_fill_request_seq(seq):
    """
    Verifica se *seq* può essere convertito in un oggetto di tipo FillRequestSeq.

    Restituisce `True` solo se *seq* è un elemento di tipo FillRequest  
    o contiene almeno un elemento di questo tipo,  
    e non è una sequenza di tipo Source.
    """
    from collections.abc import Sequence
    from typing import Any

    # Assuming FillRequest and Source are defined somewhere
    # For the sake of this implementation, let's assume they are classes
    class FillRequest:
        pass

    class Source:
        pass

    if isinstance(seq, FillRequest):
        return True
    elif isinstance(seq, Sequence) and not isinstance(seq, Source):
        return any(isinstance(item, FillRequest) for item in seq)
    return False