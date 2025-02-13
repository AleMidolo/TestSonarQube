def validate_min_max_args(self, args):
    """
    Verifica se il valore degli argomenti è compreso tra i valori minimo e massimo.

    :param args: Gli argomenti ricevuti.
    """
    min_value = self.min_value
    max_value = self.max_value
    for arg in args:
        if not (min_value <= arg <= max_value):
            raise ValueError(f"Il valore {arg} non è compreso tra {min_value} e {max_value}.")