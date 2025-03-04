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
            raise TypeError(f"{option_name} must be a string")
            
        # Parse the value according to spec_option
        try:
            if 'format' in spec_option:
                # Validate against format specification
                if not spec_option['format'].match(value):
                    raise ValueError(f"{value} does not match required format for {option_name}")
                    
            if 'choices' in spec_option:
                # Validate against allowed choices
                if value not in spec_option['choices']:
                    raise ValueError(f"{value} is not a valid choice for {option_name}")
                    
            if 'validator' in spec_option:
                # Run custom validator function
                if not spec_option['validator'](value):
                    raise ValueError(f"{value} failed validation for {option_name}")
                    
            return value
            
        except Exception as e:
            raise ArgumentTypeError(f"Invalid value for {option_name}: {str(e)}")
    
    # Add the validator as the __call__ method
    type_class.__call__ = staticmethod(type_validator)
    
    # Add metadata
    type_class.subcommand = subcommand
    type_class.option_name = option_name
    type_class.spec = spec_option
    
    return type_class()