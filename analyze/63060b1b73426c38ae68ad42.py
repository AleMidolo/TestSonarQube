import os

def inject_config(self):
    """
    Imposta la variabile d'ambiente per il percorso del file di configurazione, se non è già definita.
    """
    config_path = "/path/to/config/file"  # Replace with the actual path to your config file
    if 'CONFIG_PATH' not in os.environ:
        os.environ['CONFIG_PATH'] = config_path