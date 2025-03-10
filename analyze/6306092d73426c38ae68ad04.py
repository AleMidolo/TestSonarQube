def get_parser_option_specs(self, command_name):
    """
    Ottiene tutte le opzioni per il comando specificato

    :param command_name: il nome del comando (main, virsh, ospd, ecc...)
    :return: la lista di tutte le opzioni del comando
    """
    if not hasattr(self, '_command_parsers'):
        return []
    
    if command_name not in self._command_parsers:
        return []
    
    parser = self._command_parsers[command_name]
    return [action.option_strings for action in parser._actions if action.option_strings]