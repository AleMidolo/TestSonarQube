def get_option_spec(self, command_name, argument_name):
    """
    Ottiene la specifica per il nome dell'opzione specificato.
    """
    # Assuming self.options is a dictionary where keys are command names and values are dictionaries of argument specs
    if command_name in self.options:
        if argument_name in self.options[command_name]:
            return self.options[command_name][argument_name]
    return None