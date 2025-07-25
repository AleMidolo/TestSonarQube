def is_fill_request_seq(seq):
    """
    Verifica se *seq* può essere convertito in un oggetto di tipo FillRequestSeq.

    Restituisce `True` solo se *seq* è un elemento di tipo FillRequest  
    o contiene almeno un elemento di questo tipo,  
    e non è una sequenza di tipo Source.
    """
    # Assuming FillRequest and Source are classes or types defined elsewhere
    from typing import Sequence

    if isinstance(seq, FillRequest):
        return True
    elif isinstance(seq, Sequence) and not isinstance(seq, Source):
        return any(isinstance(item, FillRequest) for item in seq)
    return False