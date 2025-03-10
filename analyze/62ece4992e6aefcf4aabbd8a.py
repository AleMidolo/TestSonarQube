import logging
import os
import json
from typing import Dict, List, Tuple, Optional

def load_configurations(config_filenames: List[str], overrides: Optional[Dict] = None, resolve_env: bool = True) -> Tuple[Dict[str, Dict], List[logging.LogRecord]]:
    """
    根据一系列配置文件名，加载并验证每个配置文件。如果由于权限不足或解析配置文件出错导致无法读取配置文件，将记录错误日志。否则，将结果以一个元组的形式返回，包含一个将配置文件名映射到相应的解析后的配置的字典和一个包含所有解析错误的 `logging.LogRecord` 实例序列。
    """
    configs = {}
    errors = []
    
    for filename in config_filenames:
        try:
            with open(filename, 'r') as file:
                config = json.load(file)
                
                # Apply overrides if provided
                if overrides:
                    for key, value in overrides.items():
                        if key in config:
                            config[key] = value
                
                # Resolve environment variables if enabled
                if resolve_env:
                    for key, value in config.items():
                        if isinstance(value, str) and value.startswith('$'):
                            env_var = value[1:]
                            config[key] = os.getenv(env_var, value)
                
                configs[filename] = config
                
        except PermissionError:
            error_msg = f"Permission denied when trying to read {filename}"
            logging.error(error_msg)
            errors.append(logging.LogRecord(
                name=__name__,
                level=logging.ERROR,
                pathname=__file__,
                lineno=0,
                msg=error_msg,
                args=None,
                exc_info=None
            ))
        except json.JSONDecodeError:
            error_msg = f"Failed to parse JSON in {filename}"
            logging.error(error_msg)
            errors.append(logging.LogRecord(
                name=__name__,
                level=logging.ERROR,
                pathname=__file__,
                lineno=0,
                msg=error_msg,
                args=None,
                exc_info=None
            ))
        except Exception as e:
            error_msg = f"Unexpected error when loading {filename}: {str(e)}"
            logging.error(error_msg)
            errors.append(logging.LogRecord(
                name=__name__,
                level=logging.ERROR,
                pathname=__file__,
                lineno=0,
                msg=error_msg,
                args=None,
                exc_info=None
            ))
    
    return configs, errors