def create_complex_argument_type(self, subcommand, type_name, option_name, spec_option):
    """
    Crea il tipo di argomento complesso.

    :param subcommand: il nome del comando
    :param type_name: il nome del tipo complesso
    :param option_name: il nome dell'opzione
    :param spec_option: le specifiche dell'opzione
    :return: l'istanza del tipo complesso
    """
    # Assuming the complex type is a dictionary with the given specifications
    complex_type = {
        "subcommand": subcommand,
        "type_name": type_name,
        "option_name": option_name,
        "spec_option": spec_option
    }
    return complex_type