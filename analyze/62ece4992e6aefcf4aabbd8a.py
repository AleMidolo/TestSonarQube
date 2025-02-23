def load_configurations(config_filenames, overrides=None, resolve_env=True):
    import logging
    import json
    import os

    configurations = {}
    log_records = []
    logger = logging.getLogger(__name__)

    if overrides is None:
        overrides = {}

    for filename in config_filenames:
        try:
            with open(filename, 'r') as f:
                config = json.load(f)

            if resolve_env:
                config = {k: os.path.expandvars(v) for k, v in config.items()}

            # Apply overrides
            config.update(overrides)

            configurations[filename] = config

        except Exception as e:
            log_record = logger.error(f"Error loading configuration from {filename}: {e}")
            log_records.append(log_record)

    return configurations, log_records