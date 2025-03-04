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
            # Check if file exists and is readable
            config_path = Path(filename)
            if not config_path.exists():
                raise FileNotFoundError(f"Configuration file not found: {filename}")
            
            if not os.access(filename, os.R_OK):
                raise PermissionError(f"Permission denied reading configuration file: {filename}")

            # Load and parse YAML file
            with open(filename, 'r') as f:
                config = yaml.safe_load(f)

            # Apply any overrides if provided
            if overrides and isinstance(overrides, dict):
                def deep_update(d, u):
                    for k, v in u.items():
                        if isinstance(v, dict) and k in d and isinstance(d[k], dict):
                            deep_update(d[k], v)
                        else:
                            d[k] = v
                deep_update(config, overrides)

            # Resolve environment variables if requested
            if resolve_env:
                def resolve_env_vars(obj):
                    if isinstance(obj, dict):
                        return {k: resolve_env_vars(v) for k, v in obj.items()}
                    elif isinstance(obj, list):
                        return [resolve_env_vars(item) for item in obj]
                    elif isinstance(obj, str) and obj.startswith('$'):
                        env_var = obj[1:]
                        return os.environ.get(env_var, obj)
                    return obj
                
                config = resolve_env_vars(config)

            configs[filename] = config

        except FileNotFoundError as e:
            error_record = logger.makeLogRecord({
                'msg': str(e),
                'levelno': logging.ERROR,
                'exc_info': True
            })
            errors.append(error_record)
            
        except PermissionError as e:
            error_record = logger.makeLogRecord({
                'msg': str(e),
                'levelno': logging.ERROR,
                'exc_info': True
            })
            errors.append(error_record)
            
        except yaml.YAMLError as e:
            error_record = logger.makeLogRecord({
                'msg': f"Error parsing configuration file {filename}: {str(e)}",
                'levelno': logging.ERROR,
                'exc_info': True
            })
            errors.append(error_record)
            
        except Exception as e:
            error_record = logger.makeLogRecord({
                'msg': f"Unexpected error processing configuration file {filename}: {str(e)}",
                'levelno': logging.ERROR,
                'exc_info': True
            })
            errors.append(error_record)

    return configs, errors