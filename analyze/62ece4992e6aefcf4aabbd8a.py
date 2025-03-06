import logging
import os
import yaml

def load_configurations(config_filenames, overrides=None, resolve_env=True):
    """
    Dato un elenco di nomi di file di configurazione, carica e valida ciascun file di configurazione.
    Restituisci i risultati come una tupla composta da:
    - un dizionario che associa il nome del file di configurazione alla corrispondente configurazione analizzata,
    - una sequenza di istanze di `logging.LogRecord` contenenti eventuali errori di analisi.
    """
    configurations = {}
    errors = []

    for filename in config_filenames:
        try:
            with open(filename, 'r') as file:
                config = yaml.safe_load(file)
                
                if resolve_env:
                    for key, value in config.items():
                        if isinstance(value, str) and value.startswith('${') and value.endswith('}'):
                            env_var = value[2:-1]
                            config[key] = os.getenv(env_var, value)
                
                if overrides:
                    for key, value in overrides.items():
                        if key in config:
                            config[key] = value
                
                configurations[filename] = config
        except Exception as e:
            error_message = f"Error loading configuration from {filename}: {str(e)}"
            logging.error(error_message)
            errors.append(logging.LogRecord(
                name=__name__,
                level=logging.ERROR,
                pathname=filename,
                lineno=0,
                msg=error_message,
                args=None,
                exc_info=None
            ))

    return configurations, errors