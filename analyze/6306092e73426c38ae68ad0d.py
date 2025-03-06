def create_complex_argument_type(self, subcommand, type_name, option_name, spec_option):
    """
    Crea il tipo di argomento complesso.

    :param subcommand: il nome del comando
    :param type_name: il nome del tipo complesso
    :param option_name: il nome dell'opzione
    :param spec_option: le specifiche dell'opzione
    :return: l'istanza del tipo complesso
    """
    # Assuming the complex type is a class that takes the subcommand, type_name, option_name, and spec_option
    # as arguments to its constructor.
    class ComplexType:
        def __init__(self, subcommand, type_name, option_name, spec_option):
            self.subcommand = subcommand
            self.type_name = type_name
            self.option_name = option_name
            self.spec_option = spec_option

        def __repr__(self):
            return f"ComplexType(subcommand={self.subcommand}, type_name={self.type_name}, option_name={self.option_name}, spec_option={self.spec_option})"

    # Create and return an instance of the complex type
    return ComplexType(subcommand, type_name, option_name, spec_option)