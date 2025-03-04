def get_option_spec(self, command_name, argument_name):
    """
    Ottiene la specifica per il nome dell'opzione specificato.
    """
    if command_name in self.commands:
        command = self.commands[command_name]
        if 'arguments' in command and argument_name in command['arguments']:
            return command['arguments'][argument_name]
    return None