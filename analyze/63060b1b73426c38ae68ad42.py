def inject_config(self):
    """
    Imposta la variabile d'ambiente per il percorso del file di configurazione, se non è già definita.
    """
    import os

    config_path = '/path/to/config/file'  # Sostituisci con il percorso reale del file di configurazione
    if 'CONFIG_PATH' not in os.environ:
        os.environ['CONFIG_PATH'] = config_path