def is_fill_request_seq(seq):
    """
    Compruebe si *seq* puede convertirse en un FillRequestSeq.

    Devuelve `True` solo si es un elemento de tipo FillRequest  
    o contiene al menos uno de ellos,  
    y no es una secuencia de tipo Source.
    """
    from collections.abc import Sequence
    from typing import Any

    def is_fill_request(item: Any) -> bool:
        # Asumimos que FillRequest es una clase o tipo específico
        return isinstance(item, FillRequest)

    def is_source_seq(item: Any) -> bool:
        # Asumimos que Source es una clase o tipo específico
        return isinstance(item, Source)

    if is_fill_request(seq):
        return True
    elif isinstance(seq, Sequence) and not is_source_seq(seq):
        return any(is_fill_request(item) for item in seq)
    else:
        return False