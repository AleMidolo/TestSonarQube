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
            # Validate based on spec_option
            if 'pattern' in spec_option:
                import re
                if not re.match(spec_option['pattern'], value):
                    raise ValueError(f"Invalid format for {option_name}")
                    
            if 'choices' in spec_option:
                if value not in spec_option['choices']:
                    raise ValueError(f"Value must be one of: {spec_option['choices']}")
                    
            if 'min' in spec_option:
                try:
                    if float(value) < spec_option['min']:
                        raise ValueError(f"Value must be >= {spec_option['min']}")
                except ValueError:
                    raise ValueError("Value must be a number")
                    
            if 'max' in spec_option:
                try:
                    if float(value) > spec_option['max']:
                        raise ValueError(f"Value must be <= {spec_option['max']}")
                except ValueError:
                    raise ValueError("Value must be a number")
                    
            return value
            
        def __call__(self, value):
            validated_value = self.validate(value)
            return ComplexType(validated_value)
            
    # Set the type name
    ComplexType.__name__ = type_name
    
    return ComplexType