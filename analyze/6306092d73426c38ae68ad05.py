def get_option_spec(self, command_name, argument_name):
    """
    Ottiene la specifica per il nome dell'opzione specificato.
    
    :param command_name: Il nome del comando.
    :param argument_name: Il nome dell'argomento.
    :return: La specifica dell'opzione, se trovata, altrimenti None.
    """
    if hasattr(self, 'options') and command_name in self.options:
        for option in self.options[command_name]:
            if option['name'] == argument_name:
                return option
    return None