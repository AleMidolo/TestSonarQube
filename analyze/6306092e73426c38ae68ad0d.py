def create_complex_argument_type(self, subcommand, type_name, option_name,
                                 spec_option):
    """
    Crea il tipo di argomento complesso.

    :param subcommand: il nome del comando
    :param type_name: il nome del tipo complesso
    :param option_name: il nome dell'opzione
    :param spec_option: le specifiche dell'opzione
    :return: l'istanza del tipo complesso
    """
    class ComplexArgumentType:
        def __init__(self, subcommand, type_name, option_name, spec_option):
            self.subcommand = subcommand
            self.type_name = type_name
            self.option_name = option_name
            self.spec_option = spec_option

        def __repr__(self):
            return f"ComplexArgumentType(subcommand={self.subcommand}, type_name={self.type_name}, option_name={self.option_name}, spec_option={self.spec_option})"

    return ComplexArgumentType(subcommand, type_name, option_name, spec_option)