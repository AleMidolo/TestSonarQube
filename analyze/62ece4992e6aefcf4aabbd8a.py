import logging
import json
import yaml
import os

def load_configurations(config_filenames, overrides=None, resolve_env=True):
    """
    Given a sequence of configuration filenames, load and validate each configuration file. Return
    the results as a tuple of: dict of configuration filename to corresponding parsed configuration,
    and sequence of logging.LogRecord instances containing any parse errors.
    """
    configs = {}
    errors = []
    
    if overrides is None:
        overrides = {}
    
    for filename in config_filenames:
        try:
            with open(filename, 'r') as file:
                if filename.endswith('.json'):
                    config = json.load(file)
                elif filename.endswith('.yaml') or filename.endswith('.yml'):
                    config = yaml.safe_load(file)
                else:
                    errors.append(logging.LogRecord(
                        name=__name__,
                        level=logging.ERROR,
                        pathname=filename,
                        lineno=0,
                        msg=f"Unsupported file format: {filename}",
                        args=None,
                        exc_info=None
                    ))
                    continue
                
                # Apply overrides
                for key, value in overrides.items():
                    if key in config:
                        config[key] = value
                
                # Resolve environment variables if needed
                if resolve_env:
                    for key, value in config.items():
                        if isinstance(value, str) and value.startswith('$'):
                            env_var = value[1:]
                            config[key] = os.getenv(env_var, value)
                
                configs[filename] = config
                
        except Exception as e:
            errors.append(logging.LogRecord(
                name=__name__,
                level=logging.ERROR,
                pathname=filename,
                lineno=0,
                msg=f"Error loading configuration file {filename}: {str(e)}",
                args=None,
                exc_info=None
            ))
    
    return configs, errors