def get_option_spec(self, command_name, argument_name):
    """
    Ottiene la specifica per il nome dell'opzione specificato.
    """
    # Supponiamo che ci sia un dizionario di opzioni per i comandi
    options_spec = {
        'command1': {'arg1': 'spec1', 'arg2': 'spec2'},
        'command2': {'arg1': 'spec3', 'arg2': 'spec4'},
    }
    
    if command_name in options_spec:
        if argument_name in options_spec[command_name]:
            return options_spec[command_name][argument_name]
    
    return None