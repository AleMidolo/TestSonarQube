def is_fill_request_seq(seq):
    """
    Compruebe si *seq* puede convertirse en un FillRequestSeq.

    Devuelve `True` solo si es un elemento de tipo FillRequest  
    o contiene al menos uno de ellos,  
    y no es una secuencia de tipo Source.
    """
    from typing import Sequence, Any

    def is_fill_request(element: Any) -> bool:
        # Asumimos que FillRequest es una clase o tipo específico
        return isinstance(element, FillRequest)

    def is_source_seq(seq: Sequence) -> bool:
        # Asumimos que Source es una clase o tipo específico
        return all(isinstance(element, Source) for element in seq)

    if isinstance(seq, FillRequest):
        return True
    elif isinstance(seq, Sequence) and not is_source_seq(seq):
        return any(is_fill_request(element) for element in seq)
    else:
        return False