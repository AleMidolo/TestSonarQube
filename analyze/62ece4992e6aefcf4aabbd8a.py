def load_configurations(config_filenames, overrides=None, resolve_env=True):
    import logging
    import os
    import json

    logger = logging.getLogger(__name__)
    config_map = {}
    error_records = []

    for filename in config_filenames:
        try:
            if not os.path.isfile(filename):
                raise FileNotFoundError(f"Configuration file {filename} not found.")
            
            with open(filename, 'r') as file:
                config = json.load(file)

            if overrides:
                config.update(overrides)

            if resolve_env:
                for key, value in config.items():
                    if isinstance(value, str) and value.startswith('$'):
                        env_var = value[1:]
                        config[key] = os.getenv(env_var, value)

            config_map[filename] = config

        except Exception as e:
            log_record = logger.error(f"Error loading configuration from {filename}: {e}", exc_info=True)
            error_records.append(log_record)

    return config_map, error_records