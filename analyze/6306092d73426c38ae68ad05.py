def get_option_spec(self, command_name, argument_name):
    """
    Ottiene la specifica per il nome dell'opzione specificato.
    """
    # Verifica che il comando esista
    if command_name not in self.commands:
        raise ValueError(f"Command '{command_name}' not found")
        
    command = self.commands[command_name]
    
    # Cerca l'argomento nelle opzioni del comando
    for option in command.options:
        if option.name == argument_name:
            return option
            
    # Se non trova l'opzione, solleva un'eccezione
    raise ValueError(f"Option '{argument_name}' not found in command '{command_name}'")