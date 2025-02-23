def get_parser_option_specs(self, command_name):
    """
    Ottiene tutte le opzioni per il comando specificato

    :param command_name: il nome del comando (main, virsh, ospd, ecc...)
    :return: la lista di tutte le opzioni del comando
    """
    options = {
        'main': ['--help', '--version'],
        'virsh': ['--connect', '--list'],
        'ospd': ['--start', '--stop']
    }
    
    return options.get(command_name, [])