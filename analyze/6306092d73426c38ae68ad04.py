def get_parser_option_specs(self, command_name):
    """
    Obtiene todas las opciones para el comando especificado.

    :param command_name: el nombre del comando (main, virsh, ospd, etc...)
    :return: la lista de todas las opciones del comando
    """
    # Assuming self.parser is an instance of argparse.ArgumentParser or similar
    if hasattr(self, 'parser') and hasattr(self.parser, '_actions'):
        # Filter actions that are related to the specified command
        options = [action for action in self.parser._actions if action.dest == command_name]
        return options
    else:
        return []