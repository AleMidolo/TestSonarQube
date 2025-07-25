def get_option_spec(self, command_name, argument_name):
    """
    Obtiene la especificación para el nombre de opción especificado.

    Args:
        command_name (str): El nombre del comando.
        argument_name (str): El nombre del argumento.

    Returns:
        dict: La especificación de la opción si se encuentra, None en caso contrario.
    """
    if hasattr(self, 'options_spec'):
        for option in self.options_spec:
            if option.get('command') == command_name and option.get('argument') == argument_name:
                return option
    return None