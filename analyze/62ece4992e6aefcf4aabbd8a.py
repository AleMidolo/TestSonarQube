import logging
import json
import os

def load_configurations(config_filenames, overrides=None, resolve_env=True):
    """
    Dada una secuencia de nombres de archivo de configuración, carga y valida cada archivo de configuración. 
    Si el archivo de configuración no puede ser leído debido a permisos insuficientes o errores al analizar 
    el archivo de configuración, se registrará el error en el log. De lo contrario, devuelve los resultados 
    como una tupla que contiene: un diccionario que asocia el nombre del archivo de configuración con su 
    configuración analizada correspondiente, y una secuencia de instancias de `logging.LogRecord` que 
    contienen cualquier error de análisis.
    """
    configurations = {}
    log_records = []
    
    for filename in config_filenames:
        try:
            with open(filename, 'r') as file:
                if filename.endswith('.json'):
                    config = json.load(file)
                else:
                    raise ValueError(f"Unsupported file format for {filename}")
                
                if overrides:
                    config.update(overrides)
                
                if resolve_env:
                    for key, value in config.items():
                        if isinstance(value, str) and value.startswith('$'):
                            env_var = value[1:]
                            config[key] = os.getenv(env_var, value)
                
                configurations[filename] = config
        
        except Exception as e:
            log_record = logging.LogRecord(
                name='config_loader',
                level=logging.ERROR,
                pathname=filename,
                lineno=0,
                msg=str(e),
                args=None,
                exc_info=True
            )
            log_records.append(log_record)
            logging.error(f"Error loading configuration from {filename}: {e}")
    
    return configurations, log_records