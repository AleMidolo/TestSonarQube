def load_configurations(config_filenames, overrides=None, resolve_env=True):
    """
    Given a sequence of configuration filenames, load and validate each configuration file. Return
    the results as a tuple of: dict of configuration filename to corresponding parsed configuration,
    and sequence of logging.LogRecord instances containing any parse errors.
    """
    import logging
    import yaml
    import os
    
    configs = {}
    errors = []
    logger = logging.getLogger(__name__)

    for filename in config_filenames:
        try:
            with open(filename, 'r') as f:
                config = yaml.safe_load(f)
                
                # Resolve environment variables if requested
                if resolve_env and config:
                    config = _resolve_env_vars(config)
                
                # Apply any overrides
                if overrides and config:
                    config = _apply_overrides(config, overrides)
                    
                configs[filename] = config
                
        except (yaml.YAMLError, IOError) as e:
            error = logging.LogRecord(
                name=__name__,
                level=logging.ERROR,
                pathname=filename,
                lineno=0,
                msg=str(e),
                args=(),
                exc_info=None
            )
            errors.append(error)
            logger.error(f"Error loading config file {filename}: {str(e)}")
            
    return configs, errors

def _resolve_env_vars(config):
    """Helper function to resolve environment variables in config"""
    if isinstance(config, dict):
        return {k: _resolve_env_vars(v) for k, v in config.items()}
    elif isinstance(config, list):
        return [_resolve_env_vars(v) for v in config]
    elif isinstance(config, str) and config.startswith('$'):
        env_var = config[1:]
        return os.environ.get(env_var, config)
    return config

def _apply_overrides(config, overrides):
    """Helper function to apply override values to config"""
    if isinstance(config, dict) and isinstance(overrides, dict):
        for k, v in overrides.items():
            if k in config and isinstance(config[k], dict) and isinstance(v, dict):
                config[k] = _apply_overrides(config[k], v)
            else:
                config[k] = v
    return config