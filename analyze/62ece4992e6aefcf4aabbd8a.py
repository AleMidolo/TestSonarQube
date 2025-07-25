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
            with open(filename, 'r') as file:
                config = json.load(file)

            if resolve_env:
                config = {k: os.path.expandvars(v) for k, v in config.items()}

            # Apply overrides
            config.update(overrides)

            configurations[filename] = config

        except json.JSONDecodeError as e:
            log_record = logger.error(f"Error parsing {filename}: {e}")
            log_records.append(log_record)
        except FileNotFoundError:
            log_record = logger.error(f"Configuration file not found: {filename}")
            log_records.append(log_record)
        except Exception as e:
            log_record = logger.error(f"Unexpected error with {filename}: {e}")
            log_records.append(log_record)

    return configurations, log_records