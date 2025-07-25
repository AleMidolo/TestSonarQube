def get_option_spec(self, command_name, argument_name):
    """
    Ottiene la specifica per il nome dell'opzione specificato.

    :param command_name: Il nome del comando.
    :param argument_name: Il nome dell'argomento.
    :return: La specifica dell'opzione, se trovata, altrimenti None.
    """
    if not hasattr(self, 'option_specs'):
        return None

    command_specs = self.option_specs.get(command_name, {})
    return command_specs.get(argument_name, None)