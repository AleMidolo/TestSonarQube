def load_configurations(config_filenames, overrides=None, resolve_env=True):
    """
    Dada una secuencia de nombres de archivo de configuración, carga y valida cada archivo de configuración. Si el archivo de configuración no puede ser leído debido a permisos insuficientes o errores al analizar el archivo de configuración, se registrará el error en el log. De lo contrario, devuelve los resultados como una tupla que contiene: un diccionario que asocia el nombre del archivo de configuración con su configuración analizada correspondiente, y una secuencia de instancias de `logging.LogRecord` que contienen cualquier error de análisis.
    """
    import logging
    import yaml
    import os
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
            
            if not os.access(filename, os.R_OK):
                raise PermissionError(f"Permission denied reading configuration file: {filename}")

            # Load and parse YAML file
            with open(filename, 'r') as f:
                config = yaml.safe_load(f)

            # Apply any overrides if provided
            if overrides and isinstance(overrides, dict):
                config.update(overrides)

            # Resolve environment variables if requested
            if resolve_env:
                config = _resolve_env_vars(config)

            configs[filename] = config

        except (yaml.YAMLError, FileNotFoundError, PermissionError) as e:
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

def _resolve_env_vars(config):
    """Helper function to resolve environment variables in config"""
    import os
    
    if isinstance(config, dict):
        return {k: _resolve_env_vars(v) for k, v in config.items()}
    elif isinstance(config, list):
        return [_resolve_env_vars(v) for v in config]
    elif isinstance(config, str) and config.startswith('${') and config.endswith('}'):
        env_var = config[2:-1]
        return os.environ.get(env_var, config)
    else:
        return config