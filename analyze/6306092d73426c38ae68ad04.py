def get_parser_option_specs(self, command_name):
    """
    Obtiene todas las opciones para el comando especificado.

    :param command_name: el nombre del comando (main, virsh, ospd, etc...)
    :return: la lista de todas las opciones del comando
    """
    options = {
        'main': ['--help', '--version', '--verbose'],
        'virsh': ['--connect', '--list', '--start', '--shutdown'],
        'ospd': ['--config', '--status', '--restart']
    }
    
    return options.get(command_name, [])