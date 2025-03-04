def load_configurations(config_filenames, overrides=None, resolve_env=True):
    """
    Dada una secuencia de nombres de archivo de configuración, carga y valida cada archivo de configuración. Si el archivo de configuración no puede ser leído debido a permisos insuficientes o errores al analizar el archivo de configuración, se registrará el error en el log. De lo contrario, devuelve los resultados como una tupla que contiene: un diccionario que asocia el nombre del archivo de configuración con su configuración analizada correspondiente, y una secuencia de instancias de `logging.LogRecord` que contienen cualquier error de análisis.
    """
    import logging
    import os
    import yaml
    from pathlib import Path

    # Initialize return values
    configs = {}
    errors = []
    logger = logging.getLogger(__name__)

    # Process each config file
    for filename in config_filenames:
        try:
            path = Path(filename)
            
            # Check if file exists and is readable
            if not path.exists():
                raise FileNotFoundError(f"Configuration file not found: {filename}")
            
            if not os.access(path, os.R_OK):
                raise PermissionError(f"Permission denied reading configuration file: {filename}")

            # Load and parse YAML file
            with open(path, 'r') as f:
                config = yaml.safe_load(f)

            # Apply environment variable resolution if requested
            if resolve_env:
                config = resolve_environment_variables(config)

            # Apply overrides if provided
            if overrides:
                config = apply_overrides(config, overrides)

            configs[filename] = config

        except (FileNotFoundError, PermissionError, yaml.YAMLError) as e:
            error_record = logging.LogRecord(
                name=__name__,
                level=logging.ERROR,
                pathname=filename,
                lineno=0,
                msg=str(e),
                args=(),
                exc_info=None
            )
            errors.append(error_record)
            logger.error(f"Error loading configuration file {filename}: {str(e)}")

    return configs, errors

def resolve_environment_variables(config):
    """Helper function to resolve environment variables in config"""
    import os
    
    if isinstance(config, dict):
        return {k: resolve_environment_variables(v) for k, v in config.items()}
    elif isinstance(config, list):
        return [resolve_environment_variables(v) for v in config]
    elif isinstance(config, str) and config.startswith('${') and config.endswith('}'):
        env_var = config[2:-1]
        return os.environ.get(env_var, config)
    return config

def apply_overrides(config, overrides):
    """Helper function to apply configuration overrides"""
    if isinstance(config, dict) and isinstance(overrides, dict):
        for k, v in overrides.items():
            if k in config and isinstance(config[k], dict) and isinstance(v, dict):
                config[k] = apply_overrides(config[k], v)
            else:
                config[k] = v
    return config