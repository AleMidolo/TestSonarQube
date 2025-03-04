def validate_min_max_args(self, args):
    """
    Verifica si el valor de los argumentos está entre los valores mínimo y máximo.
    
    :param args: Los argumentos recibidos.
    """
    for arg_name, arg_value in args.items():
        if hasattr(self, f'min_{arg_name}') and hasattr(self, f'max_{arg_name}'):
            min_val = getattr(self, f'min_{arg_name}')
            max_val = getattr(self, f'max_{arg_name}')
            
            if not min_val <= arg_value <= max_val:
                raise ValueError(f'El valor de {arg_name} debe estar entre {min_val} y {max_val}')