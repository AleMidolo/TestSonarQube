import logging
import yaml
import os

def load_configurations(config_filenames, overrides=None, resolve_env=True):
    """
    Dada una secuencia de nombres de archivo de configuración, carga y valida cada archivo de configuración. Si el archivo de configuración no puede ser leído debido a permisos insuficientes o errores al analizar el archivo de configuración, se registrará el error en el log. De lo contrario, devuelve los resultados como una tupla que contiene: un diccionario que asocia el nombre del archivo de configuración con su configuración analizada correspondiente, y una secuencia de instancias de `logging.LogRecord` que contienen cualquier error de análisis.
    """
    configs = {}
    errors = []
    
    if overrides is None:
        overrides = {}
    
    for filename in config_filenames:
        try:
            with open(filename, 'r') as file:
                config = yaml.safe_load(file)
                
                if resolve_env:
                    for key, value in config.items():
                        if isinstance(value, str) and value.startswith('${') and value.endswith('}'):
                            env_var = value[2:-1]
                            config[key] = os.getenv(env_var, value)
                
                # Apply overrides
                for key, value in overrides.items():
                    if key in config:
                        config[key] = value
                
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
        except yaml.YAMLError as e:
            error_msg = f"Error parsing YAML in {filename}: {e}"
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
            error_msg = f"Unexpected error loading {filename}: {e}"
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