def load_configurations(config_filenames, overrides=None, resolve_env=True):
    """
    根据一系列配置文件名，加载并验证每个配置文件。如果由于权限不足或解析配置文件出错导致无法读取配置文件，将记录错误日志。否则，将结果以一个元组的形式返回，包含一个将配置文件名映射到相应的解析后的配置的字典和一个包含所有解析错误的 `logging.LogRecord` 实例序列。
    根据一系列配置文件名，加载并验证每个配置文件。将结果以一个元组的形式返回，包含一个将配置文件名映射到相应的解析后的配置的字典和一个包含所有解析错误的 `logging.LogRecord` 实例序列。
    """
    import yaml
    import os
    import logging
    from pathlib import Path

    # Initialize return values
    configs = {}
    error_logs = []
    logger = logging.getLogger(__name__)

    # Process each config file
    for filename in config_filenames:
        try:
            path = Path(filename)
            
            # Check if file exists
            if not path.exists():
                raise FileNotFoundError(f"Configuration file not found: {filename}")
                
            # Read and parse YAML file
            with open(path, 'r') as f:
                config = yaml.safe_load(f)
                
            # Resolve environment variables if requested
            if resolve_env:
                config = _resolve_env_vars(config)
                
            # Apply overrides if provided
            if overrides:
                config = _apply_overrides(config, overrides)
                
            configs[filename] = config
                
        except (PermissionError, yaml.YAMLError) as e:
            error_record = logger.makeLogRecord({
                'msg': f"Error loading configuration file {filename}: {str(e)}",
                'levelno': logging.ERROR,
                'exc_info': True
            })
            error_logs.append(error_record)
            logger.handle(error_record)

    return configs, error_logs

def _resolve_env_vars(config):
    """Helper function to resolve environment variables in config"""
    if isinstance(config, dict):
        return {k: _resolve_env_vars(v) for k, v in config.items()}
    elif isinstance(config, list):
        return [_resolve_env_vars(v) for v in config]
    elif isinstance(config, str) and config.startswith('${') and config.endswith('}'):
        env_var = config[2:-1]
        return os.environ.get(env_var, config)
    return config

def _apply_overrides(config, overrides):
    """Helper function to apply configuration overrides"""
    if isinstance(config, dict) and isinstance(overrides, dict):
        for k, v in overrides.items():
            if k in config and isinstance(config[k], dict) and isinstance(v, dict):
                config[k] = _apply_overrides(config[k], v)
            else:
                config[k] = v
    return config