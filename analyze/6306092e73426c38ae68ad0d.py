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
    
    # Add properties based on spec_option
    for key, value in spec_option.items():
        setattr(complex_type, key, value)
    
    # Add validation method
    def validate(self, value):
        if not isinstance(value, (str, int, float, bool)):
            raise ValueError(f"Invalid value type for {option_name}")
        return value
        
    setattr(complex_type, 'validate', validate)
    
    # Add string representation
    def __str__(self):
        return f"{type_name}({option_name})"
        
    setattr(complex_type, '__str__', __str__)
    
    # Create and return instance
    return complex_type()