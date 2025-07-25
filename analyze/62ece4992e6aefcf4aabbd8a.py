def load_configurations(config_filenames, overrides=None, resolve_env=True):
    import logging
    import os
    import yaml
    from pathlib import Path

    configs = {}
    errors = []
    logger = logging.getLogger(__name__)

    if overrides is None:
        overrides = {}

    for filename in config_filenames:
        try:
            path = Path(filename)
            
            if not path.exists():
                error = logging.LogRecord(
                    name=__name__,
                    level=logging.ERROR,
                    pathname=filename,
                    lineno=0,
                    msg=f"Configuration file not found: {filename}",
                    args=(),
                    exc_info=None
                )
                errors.append(error)
                continue

            if not os.access(path, os.R_OK):
                error = logging.LogRecord(
                    name=__name__,
                    level=logging.ERROR, 
                    pathname=filename,
                    lineno=0,
                    msg=f"Insufficient permissions to read configuration file: {filename}",
                    args=(),
                    exc_info=None
                )
                errors.append(error)
                continue

            with open(filename, 'r') as f:
                config = yaml.safe_load(f)

            # Apply overrides
            if filename in overrides:
                config.update(overrides[filename])

            # Resolve environment variables if requested
            if resolve_env:
                config = _resolve_env_vars(config)

            configs[filename] = config

        except yaml.YAMLError as e:
            error = logging.LogRecord(
                name=__name__,
                level=logging.ERROR,
                pathname=filename, 
                lineno=0,
                msg=f"Error parsing configuration file {filename}: {str(e)}",
                args=(),
                exc_info=None
            )
            errors.append(error)
        except Exception as e:
            error = logging.LogRecord(
                name=__name__,
                level=logging.ERROR,
                pathname=filename,
                lineno=0, 
                msg=f"Unexpected error loading configuration file {filename}: {str(e)}",
                args=(),
                exc_info=None
            )
            errors.append(error)

    return configs, errors

def _resolve_env_vars(config):
    """Helper function to resolve environment variables in config values"""
    import os
    
    if isinstance(config, dict):
        return {k: _resolve_env_vars(v) for k, v in config.items()}
    elif isinstance(config, list):
        return [_resolve_env_vars(v) for v in config]
    elif isinstance(config, str) and config.startswith('$'):
        env_var = config[1:]
        return os.environ.get(env_var, config)
    else:
        return config