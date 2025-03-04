def inject_config(self):
    """
    Imposta la variabile d'ambiente per il percorso del file di configurazione, se non è già definita.
    """
    import os
    
    # Percorso di default per il file di configurazione
    default_config_path = os.path.join(os.path.dirname(__file__), 'config.ini')
    
    # Nome della variabile d'ambiente
    env_var_name = 'CONFIG_FILE_PATH'
    
    # Controlla se la variabile d'ambiente non è già definita
    if env_var_name not in os.environ:
        # Imposta la variabile d'ambiente con il percorso di default
        os.environ[env_var_name] = default_config_path