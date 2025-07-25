def inject_config(self):
    """
    Imposta la variabile d'ambiente per il percorso del file di configurazione, se non è già definita.
    """
    import os
    
    # Percorso di default per il file di configurazione
    default_config_path = os.path.join(os.path.dirname(__file__), 'config.ini')
    
    # Verifica se la variabile d'ambiente CONFIG_PATH esiste
    if 'CONFIG_PATH' not in os.environ:
        # Se non esiste, imposta il percorso di default
        os.environ['CONFIG_PATH'] = default_config_path