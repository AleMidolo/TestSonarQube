import os

def inject_config(self):
    """
    Imposta la variabile d'ambiente per il percorso del file di configurazione, se non è già definita.
    """
    config_path = os.getenv('CONFIG_PATH')
    if config_path is None:
        os.environ['CONFIG_PATH'] = '/path/to/default/config.ini'