def get_option_spec(self, command_name, argument_name):
    """
    Ottiene la specifica per il nome dell'opzione specificato.

    :param command_name: Il nome del comando.
    :param argument_name: Il nome dell'argomento.
    :return: La specifica dell'opzione, se trovata, altrimenti None.
    """
    if hasattr(self, 'option_specs'):
        for spec in self.option_specs:
            if spec.get('command') == command_name and spec.get('argument') == argument_name:
                return spec
    return None