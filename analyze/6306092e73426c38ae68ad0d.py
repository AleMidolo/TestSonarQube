def create_complex_argumet_type(self, subcommand, type_name, option_name, spec_option):
    """
    Build the complex argument type

    :param subcommand: the command name
    :param type_name: the complex type name 
    :param option_name: the option name
    :param spec_option: option's specifications
    :return: the complex type instance
    """
    # Create a new class dynamically with the type name
    complex_type = type(type_name, (), {})
    
    # Add validation method
    def validate(cls, value):
        if not value:
            raise ValueError(f"Value required for {option_name}")
            
        # Handle different complex type validations based on spec_option
        if 'allowed_values' in spec_option:
            if value not in spec_option['allowed_values']:
                raise ValueError(f"Value {value} not in allowed values for {option_name}")
                
        if 'pattern' in spec_option:
            import re
            if not re.match(spec_option['pattern'], value):
                raise ValueError(f"Value {value} does not match pattern for {option_name}")
                
        if 'min_length' in spec_option and len(value) < spec_option['min_length']:
            raise ValueError(f"Value {value} is shorter than minimum length for {option_name}")
            
        if 'max_length' in spec_option and len(value) > spec_option['max_length']:
            raise ValueError(f"Value {value} is longer than maximum length for {option_name}")
            
        return value
        
    # Add string representation method
    def __str__(cls):
        return f"Complex argument type for {subcommand} {option_name}"
        
    # Add methods to the class
    setattr(complex_type, 'validate', classmethod(validate))
    setattr(complex_type, '__str__', classmethod(__str__))
    
    return complex_type