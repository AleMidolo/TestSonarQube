def create_complex_argument_type(self, subcommand, type_name, option_name, spec_option):
    """
    Crea il tipo di argomento complesso.

    :param subcommand: il nome del comando
    :param type_name: il nome del tipo complesso
    :param option_name: il nome dell'opzione
    :param spec_option: le specifiche dell'opzione
    :return: l'istanza del tipo complesso
    """
    # Create a custom type class dynamically
    class ComplexArgumentType:
        def __init__(self, spec):
            self.spec = spec
            
        def __call__(self, value):
            try:
                # Try to parse the value according to spec_option format/rules
                if 'format' in self.spec:
                    # Handle specific format requirements
                    if self.spec['format'] == 'key=value':
                        key, value = value.split('=')
                        return {key.strip(): value.strip()}
                    elif self.spec['format'] == 'csv':
                        return value.split(',')
                
                # Handle type conversion if specified
                if 'type' in self.spec:
                    if self.spec['type'] == 'int':
                        return int(value)
                    elif self.spec['type'] == 'float':
                        return float(value)
                    elif self.spec['type'] == 'bool':
                        return value.lower() in ('true', 'yes', '1', 'on')
                
                # Handle validation
                if 'choices' in self.spec:
                    if value not in self.spec['choices']:
                        raise ValueError(f"Value must be one of {self.spec['choices']}")
                
                if 'range' in self.spec:
                    val = float(value)
                    min_val, max_val = self.spec['range']
                    if not (min_val <= val <= max_val):
                        raise ValueError(f"Value must be between {min_val} and {max_val}")
                
                return value
                
            except Exception as e:
                raise argparse.ArgumentTypeError(
                    f"Invalid value for {option_name} in {subcommand}: {str(e)}"
                )
    
    # Return an instance of the complex argument type
    return ComplexArgumentType(spec_option)