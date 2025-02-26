def create_complex_argumet_type(self, subcommand, type_name, option_name,
                                    spec_option):
    """
    Build the complex argument type

    :param subcommand: the command name
    :param type_name: the complex type name
    :param option_name: the option name
    :param spec_option: option's specifications
    :return: the complex type instance
    """
    # Assuming we have a registry of complex types
    complex_type_registry = {
        'type1': ComplexType1,
        'type2': ComplexType2,
        # Add more complex types as needed
    }

    if type_name not in complex_type_registry:
        raise ValueError(f"Unknown type name: {type_name}")

    complex_type_class = complex_type_registry[type_name]
    complex_type_instance = complex_type_class(option_name, spec_option)

    # Additional logic can be added here based on subcommand if needed

    return complex_type_instance