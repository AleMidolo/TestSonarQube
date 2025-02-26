import json
import logging
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
    if overrides is None:
        overrides = {}

    configurations = {}
    log_records = []
    logger = logging.getLogger(__name__)

    for filename in config_filenames:
        try:
            if resolve_env:
                filename = os.path.expandvars(filename)
            with open(filename, 'r') as file:
                config = json.load(file)
                # Apply overrides
                config.update(overrides)
                configurations[filename] = config
        except (IOError, json.JSONDecodeError) as e:
            log_record = logger.error(f"Error loading configuration from {filename}: {e}")
            log_records.append(log_record)

    return configurations, log_records