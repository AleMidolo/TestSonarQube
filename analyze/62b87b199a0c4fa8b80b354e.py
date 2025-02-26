def is_fill_request_seq(seq):
    """
    Compruebe si *seq* puede convertirse en un FillRequestSeq.

    Devuelve `True` solo si es un elemento de tipo FillRequest  
    o contiene al menos uno de ellos,  
    y no es una secuencia de tipo Source.
    """
    if isinstance(seq, FillRequest):
        return True
    if isinstance(seq, Source):
        return False
    return any(isinstance(item, FillRequest) for item in seq)