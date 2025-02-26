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
    if overrides is None:
        overrides = {}

    configurations = {}
    log_records = []

    for filename in config_filenames:
        try:
            with open(filename, 'r') as file:
                config = json.load(file)
                if resolve_env:
                    config = {k: os.path.expandvars(v) for k, v in config.items()}
                configurations[filename] = {**config, **overrides}
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