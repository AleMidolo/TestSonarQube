import logging
import os
import json
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

    if overrides is None:
        overrides = {}

    for config_filename in config_filenames:
        try:
            with open(config_filename, 'r') as file:
                if config_filename.endswith('.json'):
                    config = json.load(file)
                elif config_filename.endswith('.yaml') or config_filename.endswith('.yml'):
                    config = yaml.safe_load(file)
                else:
                    errors.append(logging.LogRecord(
                        name=__name__,
                        level=logging.ERROR,
                        pathname=__file__,
                        lineno=0,
                        msg=f"Unsupported file format for {config_filename}",
                        args=None,
                        exc_info=None
                    ))
                    continue

                # Apply overrides
                for key, value in overrides.items():
                    keys = key.split('.')
                    current = config
                    for k in keys[:-1]:
                        if k in current:
                            current = current[k]
                        else:
                            current[k] = {}
                            current = current[k]
                    current[keys[-1]] = value

                # Resolve environment variables if required
                if resolve_env:
                    def resolve_env_vars(obj):
                        if isinstance(obj, dict):
                            return {k: resolve_env_vars(v) for k, v in obj.items()}
                        elif isinstance(obj, list):
                            return [resolve_env_vars(v) for v in obj]
                        elif isinstance(obj, str) and obj.startswith('${') and obj.endswith('}'):
                            env_var = obj[2:-1]
                            return os.getenv(env_var, obj)
                        return obj

                    config = resolve_env_vars(config)

                configurations[config_filename] = config

        except Exception as e:
            errors.append(logging.LogRecord(
                name=__name__,
                level=logging.ERROR,
                pathname=__file__,
                lineno=0,
                msg=f"Error loading configuration from {config_filename}: {str(e)}",
                args=None,
                exc_info=None
            ))

    return configurations, errors