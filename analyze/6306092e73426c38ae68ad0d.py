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
    class ComplexType:
        def __init__(self, value):
            self.value = value
            
        def __str__(self):
            return str(self.value)
            
        @staticmethod
        def validate(value):
            try:
                # Check if value matches specification
                if 'pattern' in spec_option:
                    import re
                    if not re.match(spec_option['pattern'], value):
                        raise ValueError(f"Value does not match pattern {spec_option['pattern']}")
                
                # Check value constraints
                if 'min' in spec_option and value < spec_option['min']:
                    raise ValueError(f"Value must be >= {spec_option['min']}")
                if 'max' in spec_option and value > spec_option['max']:
                    raise ValueError(f"Value must be <= {spec_option['max']}")
                    
                # Check allowed values
                if 'choices' in spec_option and value not in spec_option['choices']:
                    raise ValueError(f"Value must be one of {spec_option['choices']}")
                    
                return value
                
            except Exception as e:
                raise argparse.ArgumentTypeError(str(e))
    
    # Create type converter function
    def type_converter(value):
        try:
            # Convert value to appropriate Python type
            if type_name == 'int':
                value = int(value)
            elif type_name == 'float': 
                value = float(value)
            elif type_name == 'bool':
                value = value.lower() in ('true', 't', 'yes', 'y', '1')
                
            # Validate converted value
            return ComplexType.validate(value)
            
        except ValueError as e:
            raise argparse.ArgumentTypeError(f"Invalid {option_name}: {str(e)}")
            
    return type_converter