def load_configurations(config_filenames, overrides=None, resolve_env=True):
    import logging
    import os
    import json

    logger = logging.getLogger(__name__)
    error_records = []
    configurations = {}

    for filename in config_filenames:
        try:
            if not os.access(filename, os.R_OK):
                raise PermissionError(f"Permission denied: {filename}")

            with open(filename, 'r') as file:
                config = json.load(file)

            if overrides:
                config.update(overrides)

            if resolve_env:
                for key, value in config.items():
                    if isinstance(value, str) and value.startswith('$'):
                        env_var = value[1:]
                        config[key] = os.getenv(env_var, value)

            configurations[filename] = config

        except (FileNotFoundError, json.JSONDecodeError, PermissionError) as e:
            log_record = logger.error(f"Error loading configuration from {filename}: {e}")
            error_records.append(log_record)

    return configurations, error_records