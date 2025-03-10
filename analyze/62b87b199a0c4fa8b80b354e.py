def is_fill_request_seq(seq):
    """
    Verifica se *seq* può essere convertito in un oggetto di tipo FillRequestSeq.

    Restituisce `True` solo se *seq* è un elemento di tipo FillRequest  
    o contiene almeno un elemento di questo tipo,  
    e non è una sequenza di tipo Source.
    """
    from collections.abc import Sequence
    from typing import Type

    # Supponiamo che FillRequest e Source siano classi definite altrove
    FillRequest = Type('FillRequest')  # Placeholder per la classe FillRequest
    Source = Type('Source')  # Placeholder per la classe Source

    if isinstance(seq, FillRequest):
        return True
    elif isinstance(seq, Sequence) and not isinstance(seq, Source):
        return any(isinstance(item, FillRequest) for item in seq)
    else:
        return False