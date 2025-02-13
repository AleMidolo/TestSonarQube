import logging
import os
import json

def load_configurations(config_filenames, overrides=None, resolve_env=True):
    if overrides is None:
        overrides = {}
    
    configurations = {}
    log_records = []
    logger = logging.getLogger(__name__)

    for filename in config_filenames:
        try:
            if resolve_env:
                filename = os.path.expandvars(filename)
            with open(filename, 'r') as file:
                config = json.load(file)
                config.update(overrides)
                configurations[filename] = config
        except (IOError, json.JSONDecodeError) as e:
            log_record = logger.error(f"Error loading configuration from {filename}: {e}")
            log_records.append(log_record)

    return configurations, log_records