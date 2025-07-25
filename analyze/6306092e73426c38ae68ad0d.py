def create_complex_argument_type(self, subcommand, type_name, option_name, spec_option):
    """
    Crea il tipo di argomento complesso.

    :param subcommand: il nome del comando
    :param type_name: il nome del tipo complesso
    :param option_name: il nome dell'opzione
    :param spec_option: le specifiche dell'opzione
    :return: l'istanza del tipo complesso
    """
    # Create a custom argument type class
    class ComplexArgumentType:
        def __init__(self, spec):
            self.spec = spec
            
        def __call__(self, value):
            try:
                # Try to parse the value according to spec
                if self.spec.get('type') == 'integer':
                    return int(value)
                elif self.spec.get('type') == 'float':
                    return float(value)
                elif self.spec.get('type') == 'boolean':
                    return value.lower() in ('true', 't', 'yes', 'y', '1')
                elif self.spec.get('type') == 'list':
                    return value.split(',')
                elif self.spec.get('type') == 'dict':
                    pairs = value.split(',')
                    return dict(pair.split(':') for pair in pairs)
                else:
                    # Default to string
                    return str(value)
                    
            except (ValueError, TypeError) as e:
                raise argparse.ArgumentTypeError(
                    f"Invalid value for {option_name} in {subcommand}: {str(e)}"
                )
            
        def __repr__(self):
            return f'ComplexArgumentType({type_name})'
            
    # Return an instance of the custom type
    return ComplexArgumentType(spec_option)