def load_configurations(config_filenames, overrides=None, resolve_env=True):
    import logging
    import json
    import os

    if overrides is None:
        overrides = {}

    configurations = {}
    log_records = []

    for filename in config_filenames:
        try:
            with open(filename, 'r') as file:
                config = json.load(file)

            if resolve_env:
                for key, value in config.items():
                    if isinstance(value, str) and value.startswith('$'):
                        env_var = value[1:]
                        config[key] = os.getenv(env_var, value)

            configurations[filename] = {**config, **overrides}

        except json.JSONDecodeError as e:
            log_records.append(logging.LogRecord(
                name='config_loader',
                level=logging.ERROR,
                pathname=filename,
                lineno=0,
                msg=f"Error parsing {filename}: {str(e)}",
                args=None,
                exc_info=None
            ))
        except FileNotFoundError:
            log_records.append(logging.LogRecord(
                name='config_loader',
                level=logging.ERROR,
                pathname=filename,
                lineno=0,
                msg=f"File not found: {filename}",
                args=None,
                exc_info=None
            ))
        except Exception as e:
            log_records.append(logging.LogRecord(
                name='config_loader',
                level=logging.ERROR,
                pathname=filename,
                lineno=0,
                msg=f"Unexpected error with {filename}: {str(e)}",
                args=None,
                exc_info=None
            ))

    return configurations, log_records