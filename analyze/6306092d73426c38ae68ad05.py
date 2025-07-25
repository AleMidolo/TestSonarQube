def get_option_spec(self, command_name, argument_name):
    """
    Obtiene la especificación para el nombre de opción especificado.

    Args:
        command_name (str): El nombre del comando.
        argument_name (str): El nombre del argumento.

    Returns:
        dict: La especificación de la opción si se encuentra, None en caso contrario.
    """
    # Asumiendo que self.options es un diccionario que contiene las especificaciones de las opciones
    if hasattr(self, 'options') and isinstance(self.options, dict):
        command_options = self.options.get(command_name, {})
        return command_options.get(argument_name, None)
    return None