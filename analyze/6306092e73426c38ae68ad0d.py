def create_complex_argumet_type(self, subcommand, type_name, option_name, spec_option):
    """
    जटिल आर्गुमेंट प्रकार (complex argument type) बनाएं

    :param subcommand: कमांड का नाम
    :param type_name: जटिल प्रकार का नाम (complex type name) 
    :param option_name: विकल्प का नाम (option name)
    :param spec_option: विकल्प की विशिष्टताएँ (option's specifications)
    :return: जटिल प्रकार का उदाहरण (complex type instance)
    """
    # Create a new class dynamically for the complex type
    complex_type = type(type_name, (), {})
    
    # Add validation method
    def validate(self, value):
        if not isinstance(value, str):
            raise ValueError(f"Value for {option_name} must be a string")
        
        # Apply any specific validation rules from spec_option
        if 'min_length' in spec_option:
            if len(value) < spec_option['min_length']:
                raise ValueError(f"{option_name} must be at least {spec_option['min_length']} characters long")
                
        if 'max_length' in spec_option:
            if len(value) > spec_option['max_length']:
                raise ValueError(f"{option_name} cannot exceed {spec_option['max_length']} characters")
                
        if 'pattern' in spec_option:
            import re
            if not re.match(spec_option['pattern'], value):
                raise ValueError(f"{option_name} does not match required pattern {spec_option['pattern']}")
        
        return value
    
    # Add string representation method
    def __str__(self):
        return f"Complex argument type for {subcommand}:{option_name}"
    
    # Add methods to the class
    complex_type.validate = validate
    complex_type.__str__ = __str__
    
    # Create and return an instance
    return complex_type()