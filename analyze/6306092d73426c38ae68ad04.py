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
    
    # Aquí se asume que hay un método para obtener las especificaciones del parser
    # dependiendo del comando. Esto es un ejemplo genérico.
    parser_specs = self._get_parser_specs_for_command(command_name)
    self._command_parser_specs[command_name] = parser_specs
    return parser_specs