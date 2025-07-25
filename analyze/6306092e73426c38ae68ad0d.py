def create_complex_argument_type(self, subcommand, type_name, option_name, spec_option):
    """
    Construye el tipo de argumento complejo.

    :param subcommand: el nombre del comando
    :param type_name: el nombre del tipo complejo
    :param option_name: el nombre de la opción
    :param spec_option: las especificaciones de la opción
    :return: la instancia del tipo complejo
    """
    class ComplexArgumentType:
        def __init__(self, name, specs):
            self.name = name
            self.specs = specs

        def __repr__(self):
            return f"<ComplexArgumentType name={self.name}, specs={self.specs}>"

    return ComplexArgumentType(type_name, spec_option)