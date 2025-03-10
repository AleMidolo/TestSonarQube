def create_complex_argumet_type(self, subcommand, type_name, option_name, spec_option):
    """
    Build the complex argument type

    :param subcommand: the command name
    :param type_name: the complex type name
    :param option_name: the option name
    :param spec_option: option's specifications
    :return: the complex type instance
    """
    # Assuming the complex type is a dictionary with the given specifications
    complex_type = {
        "subcommand": subcommand,
        "type_name": type_name,
        "option_name": option_name,
        "spec_option": spec_option
    }
    return complex_type