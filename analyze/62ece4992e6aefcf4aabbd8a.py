import logging
import json
import os
from typing import Dict, List, Tuple, Optional, Sequence

def load_configurations(config_filenames: Sequence[str], overrides: Optional[Dict] = None, resolve_env: bool = True) -> Tuple[Dict[str, Dict], List[logging.LogRecord]]:
    """
    Given a sequence of configuration filenames, load and validate each configuration file. Return
    the results as a tuple of: dict of configuration filename to corresponding parsed configuration,
    and sequence of logging.LogRecord instances containing any parse errors.
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
            error_msg = f"Error parsing {filename}: {str(e)}"
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
            error_msg = f"Unexpected error loading {filename}: {str(e)}"
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