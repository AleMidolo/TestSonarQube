def get_option_spec(self, command_name, argument_name):
    """
    Obtiene la especificación para el nombre de opción especificado.
    """
    # Verificar que el comando existe
    if command_name not in self.commands:
        return None
        
    command = self.commands[command_name]
    
    # Buscar el argumento en las opciones del comando
    if argument_name in command.options:
        return command.options[argument_name]
        
    # Si no se encuentra, retornar None
    return None