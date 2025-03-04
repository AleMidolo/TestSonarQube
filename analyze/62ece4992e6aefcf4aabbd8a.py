import json
import logging
import os

def load_configurations(config_filenames, overrides=None, resolve_env=True):
    """
    Dato un elenco di nomi di file di configurazione, carica e valida ciascun file di configurazione.
    Restituisci i risultati come una tupla composta da:
    - un dizionario che associa il nome del file di configurazione alla corrispondente configurazione analizzata,
    - una sequenza di istanze di `logging.LogRecord` contenenti eventuali errori di analisi.
    """
    if overrides is None:
        overrides = {}

    configurations = {}
    log_records = []
    logger = logging.getLogger(__name__)

    for filename in config_filenames:
        try:
            with open(filename, 'r') as f:
                config = json.load(f)
                if resolve_env:
                    config = {k: os.path.expandvars(v) for k, v in config.items()}
                configurations[filename] = {**config, **overrides}
        except Exception as e:
            log_record = logger.error(f"Error loading configuration from {filename}: {e}")
            log_records.append(log_record)

    return configurations, log_records