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
                if 'choices' in self.spec:
                    if value not in self.spec['choices']:
                        raise ValueError(f"Value must be one of {self.spec['choices']}")
                
                if 'type' in self.spec:
                    value = self.spec['type'](value)
                    
                if 'validator' in self.spec:
                    if not self.spec['validator'](value):
                        raise ValueError(f"Value {value} failed validation")
                        
                return value
                
            except Exception as e:
                raise argparse.ArgumentTypeError(
                    f"Invalid value for {option_name}: {str(e)}"
                )
                
    # Create instance with the provided specs
    return ComplexArgumentType(spec_option)