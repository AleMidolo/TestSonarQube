import logging
import os
import yaml
from typing import Dict, List, Tuple, Optional, Sequence

def load_configurations(config_filenames: List[str], overrides: Optional[Dict] = None, resolve_env: bool = True) -> Tuple[Dict[str, Dict], Sequence[logging.LogRecord]]:
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
                config_data = yaml.safe_load(file)
                
                if resolve_env:
                    for key, value in config_data.items():
                        if isinstance(value, str) and value.startswith('${') and value.endswith('}'):
                            env_var = value[2:-1]
                            config_data[key] = os.getenv(env_var, value)
                
                if overrides:
                    config_data.update(overrides)
                
                configurations[config_filename] = config_data
        except Exception as e:
            error_message = f"Error loading configuration from {config_filename}: {str(e)}"
            errors.append(logging.LogRecord(
                name=__name__,
                level=logging.ERROR,
                pathname=__file__,
                lineno=0,
                msg=error_message,
                args=None,
                exc_info=None
            ))

    return configurations, errors