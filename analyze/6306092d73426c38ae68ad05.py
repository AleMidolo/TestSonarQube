def get_option_spec(self, command_name, argument_name):
    """
    Ottiene la specifica per il nome dell'opzione specificato.
    """
    # Verifica che il comando esista
    if command_name not in self.commands:
        raise ValueError(f"Command '{command_name}' not found")
        
    command = self.commands[command_name]
    
    # Cerca l'argomento nelle opzioni del comando
    if argument_name not in command.options:
        raise ValueError(f"Option '{argument_name}' not found for command '{command_name}'")
        
    # Restituisce la specifica dell'opzione
    return command.options[argument_name]