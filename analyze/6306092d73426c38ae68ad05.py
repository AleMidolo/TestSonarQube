def get_option_spec(self, command_name, argument_name):
    """
    Ottiene la specifica per il nome dell'opzione specificato.
    """
    # Assuming there's a dictionary that holds command options
    command_options = {
        'command1': {'arg1': 'spec1', 'arg2': 'spec2'},
        'command2': {'arg1': 'spec3', 'arg2': 'spec4'},
    }
    
    if command_name in command_options:
        if argument_name in command_options[command_name]:
            return command_options[command_name][argument_name]
    
    return None