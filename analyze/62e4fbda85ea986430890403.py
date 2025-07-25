import random

def _shuffled(seq: Sequence[str]) -> list[str]:
    """
    Barajar de manera determinista.
    """
    # Usar una semilla fija para asegurar que el barajado sea determinista
    random.seed(42)
    shuffled_seq = list(seq)  # Convertir a lista para poder barajar
    random.shuffle(shuffled_seq)
    return shuffled_seq