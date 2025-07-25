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
    type_class = type(type_name, (), {})
    
    def type_validator(value):
        # Check if value matches the specification
        if not isinstance(value, str):
            raise ValueError(f"{option_name} must be a string")
            
        # Parse the value according to spec_option
        if 'format' in spec_option:
            try:
                # Try to validate against format
                if not spec_option['format'].match(value):
                    raise ValueError(f"{option_name} does not match required format")
            except:
                raise ValueError(f"Invalid format for {option_name}")
                
        if 'choices' in spec_option:
            if value not in spec_option['choices']:
                raise ValueError(f"{option_name} must be one of {spec_option['choices']}")
                
        if 'min_length' in spec_option:
            if len(value) < spec_option['min_length']:
                raise ValueError(f"{option_name} must be at least {spec_option['min_length']} characters")
                
        if 'max_length' in spec_option:
            if len(value) > spec_option['max_length']:
                raise ValueError(f"{option_name} must be at most {spec_option['max_length']} characters")
        
        return value

    # Add the validator as a class method
    setattr(type_class, '__call__', staticmethod(type_validator))
    
    # Add metadata
    type_class.subcommand = subcommand
    type_class.option_name = option_name
    type_class.spec = spec_option
    
    return type_class()