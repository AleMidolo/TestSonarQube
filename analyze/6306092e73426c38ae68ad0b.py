def validate_min_max_args(self, args):
    """
    Verifica se il valore degli argomenti è compreso tra i valori minimo e massimo.

    :param args: Gli argomenti ricevuti.
    """
    for arg_name, arg_value in args.items():
        if hasattr(self, f'min_{arg_name}') and hasattr(self, f'max_{arg_name}'):
            min_val = getattr(self, f'min_{arg_name}')
            max_val = getattr(self, f'max_{arg_name}')
            
            if not min_val <= arg_value <= max_val:
                raise ValueError(f"Il valore di {arg_name} deve essere compreso tra {min_val} e {max_val}")