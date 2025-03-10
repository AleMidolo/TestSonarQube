def is_fill_request_seq(seq):
    """
    Compruebe si *seq* puede convertirse en un FillRequestSeq.

    Devuelve `True` solo si es un elemento de tipo FillRequest  
    o contiene al menos uno de ellos,  
    y no es una secuencia de tipo Source.
    """
    # Assuming FillRequest and Source are defined classes or types
    from typing import Sequence, Any

    def is_fill_request(item: Any) -> bool:
        # Replace with actual check for FillRequest type
        return isinstance(item, FillRequest)

    def is_source(item: Any) -> bool:
        # Replace with actual check for Source type
        return isinstance(item, Source)

    if is_fill_request(seq):
        return True
    elif isinstance(seq, Sequence) and not isinstance(seq, str):
        return any(is_fill_request(item) for item in seq) and not any(is_source(item) for item in seq)
    else:
        return False