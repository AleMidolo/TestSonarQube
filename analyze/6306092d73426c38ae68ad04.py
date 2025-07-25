def get_parser_option_specs(self, command_name):
    """
    Ottiene tutte le opzioni per il comando specificato

    :param command_name: il nome del comando (main, virsh, ospd, ecc...)
    :return: la lista di tutte le opzioni del comando
    """
    if not hasattr(self, '_parser_options'):
        self._parser_options = {}
    
    if command_name in self._parser_options:
        return self._parser_options[command_name]
    
    # Simulate fetching options for the command
    # This is a placeholder implementation
    options = []
    if command_name == "main":
        options = ["--help", "--version", "--verbose"]
    elif command_name == "virsh":
        options = ["--connect", "--list", "--details"]
    elif command_name == "ospd":
        options = ["--config", "--log-level", "--daemon"]
    else:
        options = ["--option1", "--option2", "--option3"]
    
    self._parser_options[command_name] = options
    return options