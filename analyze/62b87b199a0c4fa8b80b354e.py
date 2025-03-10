def is_fill_request_seq(seq):
    """
    Compruebe si *seq* puede convertirse en un FillRequestSeq.

    Devuelve `True` solo si es un elemento de tipo FillRequest  
    o contiene al menos uno de ellos,  
    y no es una secuencia de tipo Source.
    """
    # Assuming FillRequest and Source are classes or types defined elsewhere
    from typing import Sequence

    if isinstance(seq, FillRequest):
        return True
    elif isinstance(seq, Sequence) and not isinstance(seq, Source):
        return any(isinstance(item, FillRequest) for item in seq)
    return False