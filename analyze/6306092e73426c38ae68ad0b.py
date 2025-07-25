def validate_min_max_args(self, args):
    """
    Verifica se il valore degli argomenti è compreso tra i valori minimo e massimo.

    :param args: Gli argomenti ricevuti.
    """
    min_value = 0  # Imposta il valore minimo
    max_value = 100  # Imposta il valore massimo
    
    for arg in args:
        if not (min_value <= arg <= max_value):
            raise ValueError(f"Valore {arg} non compreso tra {min_value} e {max_value}")
    
    return True