def get_option_spec(self, command_name, argument_name):
    """
    Ottiene la specifica per il nome dell'opzione specificato.
    """
    # Verifica che il comando esista
    if command_name not in self.commands:
        return None
        
    command = self.commands[command_name]
    
    # Cerca l'argomento nelle opzioni del comando
    if 'options' in command and argument_name in command['options']:
        return command['options'][argument_name]
        
    # Se non trovato nelle opzioni specifiche del comando,
    # cerca nelle opzioni globali
    if hasattr(self, 'global_options') and argument_name in self.global_options:
        return self.global_options[argument_name]
        
    return None