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
        def __init__(self, name, specs):
            self.name = name
            self.specs = specs

        def __repr__(self):
            return f"ComplexArgumentType(name={self.name}, specs={self.specs})"

    # Create an instance of the complex argument type
    complex_type_instance = ComplexArgumentType(type_name, spec_option)
    
    # Here you can add any additional logic related to subcommand or option_name if needed

    return complex_type_instance