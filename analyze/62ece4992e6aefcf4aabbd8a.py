import logging
import json
import os
from typing import Dict, List, Tuple, Optional

def load_configurations(config_filenames: List[str], overrides: Optional[Dict] = None, resolve_env: bool = True) -> Tuple[Dict[str, Dict], List[logging.LogRecord]]:
    """
    Load and validate each configuration file given a sequence of configuration filenames.
    Return the result as a tuple containing:
    1. A dictionary of configuration filenames and their corresponding parsed configurations.
    2. A sequence of `logging.LogRecord` instances containing any parsing errors.
    """
    configurations = {}
    errors = []
    
    for filename in config_filenames:
        try:
            with open(filename, 'r') as file:
                config = json.load(file)
                
                if resolve_env:
                    for key, value in config.items():
                        if isinstance(value, str) and value.startswith('$'):
                            env_var = value[1:]
                            config[key] = os.getenv(env_var, value)
                
                if overrides:
                    config.update(overrides)
                
                configurations[filename] = config
        except json.JSONDecodeError as e:
            error_msg = f"JSON parsing error in file {filename}: {str(e)}"
            logging.error(error_msg)
            errors.append(logging.LogRecord(
                name=__name__,
                level=logging.ERROR,
                pathname=filename,
                lineno=0,
                msg=error_msg,
                args=None,
                exc_info=None
            ))
        except Exception as e:
            error_msg = f"Error loading configuration file {filename}: {str(e)}"
            logging.error(error_msg)
            errors.append(logging.LogRecord(
                name=__name__,
                level=logging.ERROR,
                pathname=filename,
                lineno=0,
                msg=error_msg,
                args=None,
                exc_info=None
            ))
    
    return configurations, errors