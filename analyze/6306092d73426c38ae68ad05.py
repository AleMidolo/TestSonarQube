def get_option_spec(self, command_name, argument_name):
    """
    Ottiene la specifica per il nome dell'opzione specificato.

    :param command_name: Il nome del comando.
    :param argument_name: Il nome dell'argomento.
    :return: La specifica dell'opzione, se trovata, altrimenti None.
    """
    if hasattr(self, 'options') and isinstance(self.options, dict):
        command_options = self.options.get(command_name, {})
        return command_options.get(argument_name, None)
    return None