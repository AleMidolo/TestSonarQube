def is_fill_request_seq(seq):
    """
    Compruebe si *seq* puede convertirse en un FillRequestSeq.

    Devuelve `True` solo si es un elemento de tipo FillRequest  
    o contiene al menos uno de ellos,  
    y no es una secuencia de tipo Source.
    """
    # Assuming FillRequest and Source are classes or types defined elsewhere
    from typing import Sequence, Any

    def is_fill_request(item: Any) -> bool:
        return isinstance(item, FillRequest)

    def is_source(item: Any) -> bool:
        return isinstance(item, Source)

    if isinstance(seq, Sequence):
        if any(is_fill_request(item) for item in seq):
            return not all(is_source(item) for item in seq)
        else:
            return False
    else:
        return is_fill_request(seq) and not is_source(seq)