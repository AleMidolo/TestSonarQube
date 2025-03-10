def get_parser_option_specs(self, command_name):
    """
    Obtiene todas las opciones para el comando especificado.

    :param command_name: el nombre del comando (main, virsh, ospd, etc...)
    :return: la lista de todas las opciones del comando
    """
    if not hasattr(self, '_command_parsers'):
        return []
    
    if command_name not in self._command_parsers:
        return []
    
    parser = self._command_parsers[command_name]
    return [option for option in parser._actions if option.dest != 'help']