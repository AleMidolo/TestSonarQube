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

    def is_source_seq(seq: Sequence) -> bool:
        return isinstance(seq, Source)

    if is_source_seq(seq):
        return False

    if is_fill_request(seq):
        return True

    if isinstance(seq, Sequence):
        return any(is_fill_request(item) for item in seq)

    return False