def is_fill_request_seq(seq):
    """
    Verifica se *seq* può essere convertito in un oggetto di tipo FillRequestSeq.

    Restituisce `True` solo se *seq* è un elemento di tipo FillRequest  
    o contiene almeno un elemento di questo tipo,  
    e non è una sequenza di tipo Source.
    """
    if isinstance(seq, Source):
        return False
    if isinstance(seq, FillRequest):
        return True
    if isinstance(seq, (list, tuple)):
        return any(isinstance(item, FillRequest) for item in seq)
    return False