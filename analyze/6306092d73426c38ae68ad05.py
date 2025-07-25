def get_option_spec(self, command_name, argument_name):
    """
    Obtiene la especificación para el nombre de opción especificado.
    """
    # Verificar que el comando existe
    if command_name not in self.commands:
        raise ValueError(f"Command '{command_name}' not found")
        
    command = self.commands[command_name]
    
    # Buscar el argumento en las opciones del comando
    if argument_name not in command.options:
        raise ValueError(f"Option '{argument_name}' not found for command '{command_name}'")
        
    # Retornar la especificación de la opción
    return command.options[argument_name]