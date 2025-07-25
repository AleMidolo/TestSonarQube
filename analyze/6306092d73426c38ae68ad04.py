def get_parser_option_specs(self, command_name):
    """
    Ottiene tutte le opzioni per il comando specificato

    :param command_name: il nome del comando (main, virsh, ospd, ecc...)
    :return: la lista di tutte le opzioni del comando
    """
    # Assuming self.parser is an instance of argparse.ArgumentParser or similar
    if hasattr(self, 'parser') and hasattr(self.parser, '_actions'):
        # Filter actions that are related to the specified command
        options = [action for action in self.parser._actions if command_name in action.option_strings]
        return options
    else:
        return []