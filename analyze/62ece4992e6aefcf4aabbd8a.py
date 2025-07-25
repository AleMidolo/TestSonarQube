import logging
import os
import json
import yaml
from typing import Dict, List, Tuple, Optional, Union

def load_configurations(config_filenames: List[str], overrides: Optional[Dict] = None, resolve_env: bool = True) -> Tuple[Dict[str, Dict], List[logging.LogRecord]]:
    """
    Dato un elenco di nomi di file di configurazione, carica e valida ciascun file di configurazione.
    Restituisci i risultati come una tupla composta da:
    - un dizionario che associa il nome del file di configurazione alla corrispondente configurazione analizzata,
    - una sequenza di istanze di `logging.LogRecord` contenenti eventuali errori di analisi.
    """
    configurations = {}
    errors = []

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

                if resolve_env:
                    config = _resolve_env_vars(config)

                if overrides:
                    config.update(overrides)

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

def _resolve_env_vars(config: Union[Dict, List, str]) -> Union[Dict, List, str]:
    """
    Resolve environment variables in the configuration.
    """
    if isinstance(config, dict):
        return {key: _resolve_env_vars(value) for key, value in config.items()}
    elif isinstance(config, list):
        return [_resolve_env_vars(item) for item in config]
    elif isinstance(config, str) and config.startswith('${') and config.endswith('}'):
        env_var = config[2:-1]
        return os.getenv(env_var, config)
    else:
        return config