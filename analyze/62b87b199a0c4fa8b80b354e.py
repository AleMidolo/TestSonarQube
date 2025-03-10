def is_fill_request_seq(seq):
    """
    Comprueba si *seq* puede convertirse en un FillRequestSeq.

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
        return any(is_fill_request(item) for item in seq) and not is_source(seq)
    else:
        return is_fill_request(seq) and not is_source(seq)