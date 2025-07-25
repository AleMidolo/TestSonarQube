def create_complex_argument_type(self, subcommand, type_name, option_name, spec_option):
    """
    Construye el tipo de argumento complejo.

    :param subcommand: el nombre del comando
    :param type_name: el nombre del tipo complejo
    :param option_name: el nombre de la opción
    :param spec_option: las especificaciones de la opción
    :return: la instancia del tipo complejo
    """
    # Crear una instancia del tipo complejo basado en las especificaciones
    complex_type = {
        "subcommand": subcommand,
        "type_name": type_name,
        "option_name": option_name,
        "spec_option": spec_option
    }
    return complex_type