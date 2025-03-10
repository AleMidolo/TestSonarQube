import logging
import os
import json

def load_configurations(config_filenames, overrides=None, resolve_env=True):
    """
    根据一系列配置文件名，加载并验证每个配置文件。如果由于权限不足或解析配置文件出错导致无法读取配置文件，将记录错误日志。否则，将结果以一个元组的形式返回，包含一个将配置文件名映射到相应的解析后的配置的字典和一个包含所有解析错误的 `logging.LogRecord` 实例序列。
    根据一系列配置文件名，加载并验证每个配置文件。将结果以一个元组的形式返回，包含一个将配置文件名映射到相应的解析后的配置的字典和一个包含所有解析错误的 `logging.LogRecord` 实例序列。
    """
    config_dict = {}
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
                    for key, value in overrides.items():
                        if key in config:
                            config[key] = value
                
                config_dict[filename] = config
        except PermissionError:
            logging.error(f"Permission denied when trying to read {filename}")
            errors.append(logging.LogRecord(
                name=__name__,
                level=logging.ERROR,
                pathname=filename,
                lineno=0,
                msg=f"Permission denied when trying to read {filename}",
                args=None,
                exc_info=None
            ))
        except json.JSONDecodeError:
            logging.error(f"Failed to parse JSON in {filename}")
            errors.append(logging.LogRecord(
                name=__name__,
                level=logging.ERROR,
                pathname=filename,
                lineno=0,
                msg=f"Failed to parse JSON in {filename}",
                args=None,
                exc_info=None
            ))
        except Exception as e:
            logging.error(f"Unexpected error when reading {filename}: {e}")
            errors.append(logging.LogRecord(
                name=__name__,
                level=logging.ERROR,
                pathname=filename,
                lineno=0,
                msg=f"Unexpected error when reading {filename}: {e}",
                args=None,
                exc_info=None
            ))
    
    return config_dict, errors