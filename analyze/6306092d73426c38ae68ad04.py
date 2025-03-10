def get_parser_option_specs(self, command_name):
    """
    Obtiene todas las opciones para el comando especificado.

    :param command_name: el nombre del comando (main, virsh, ospd, etc...)
    :return: la lista de todas las opciones del comando
    """
    if not hasattr(self, '_command_parser_specs'):
        self._command_parser_specs = {}

    if command_name in self._command_parser_specs:
        return self._command_parser_specs[command_name]
    else:
        return []