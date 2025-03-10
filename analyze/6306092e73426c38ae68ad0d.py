def create_complex_argumet_type(self, subcommand, type_name, option_name, spec_option):
    """
    जटिल आर्गुमेंट प्रकार (complex argument type) बनाएं

    :param subcommand: कमांड का नाम
    :param type_name: जटिल प्रकार का नाम (complex type name)
    :param option_name: विकल्प का नाम (option name)
    :param spec_option: विकल्प की विशिष्टताएँ (option's specifications)
    :return: जटिल प्रकार का उदाहरण (complex type instance)
    """
    # Create a dictionary to represent the complex argument type
    complex_type = {
        "subcommand": subcommand,
        "type_name": type_name,
        "option_name": option_name,
        "spec_option": spec_option
    }
    
    # Return the complex type instance
    return complex_type