import random

def _shuffled(seq: Sequence[str]) -> list[str]:
    """
    Barajar de manera determinista.
    """
    # Convertir la secuencia a una lista para asegurar que sea mutable
    seq_list = list(seq)
    # Usar una semilla fija para asegurar que el barajado sea determinista
    random.seed(42)
    random.shuffle(seq_list)
    return seq_list