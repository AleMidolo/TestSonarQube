def get_option_spec(self, command_name, argument_name):
    """
    Obtiene la especificación para el nombre de opción especificado.

    :param command_name: Nombre del comando.
    :param argument_name: Nombre del argumento.
    :return: Especificación de la opción.
    """
    # Aquí se asume que self.options es un diccionario que contiene las especificaciones de las opciones
    # La estructura podría ser algo como: self.options = {"command_name": {"argument_name": "spec"}}
    if command_name in self.options:
        if argument_name in self.options[command_name]:
            return self.options[command_name][argument_name]
    return None