def inject_config(self):
    """
    Imposta la variabile d'ambiente per il percorso del file di configurazione, se non è già definita.
    """
    import os
    
    if 'CONFIG_PATH' not in os.environ:
        default_config_path = os.path.join(os.path.dirname(__file__), 'config.ini')
        os.environ['CONFIG_PATH'] = default_config_path