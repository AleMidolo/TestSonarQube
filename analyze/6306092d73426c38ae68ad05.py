def get_option_spec(self, command_name, argument_name):
    """
    Obtiene la especificación para el nombre de opción especificado.
    """
    # Assuming self.options is a dictionary where keys are command names and values are dictionaries
    # of argument specifications.
    if command_name in self.options:
        if argument_name in self.options[command_name]:
            return self.options[command_name][argument_name]
    return None