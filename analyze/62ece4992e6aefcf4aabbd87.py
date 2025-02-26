import logging
import os

def build_app_logger(name='app', logfile='app.log', debug=True):
    """
    "Logger" de aplicaciones de propósito general. Útil principalmente para depuración.

    Args:
        name: El nombre del logger.
        logfile: El archivo de registro donde se guardarán los logs.
        debug: Indica si es necesario habilitar la depuración.

    Returns:
        Devuelve un objeto de registrador (logger) instanciado.
    """
    # Crear el directorio para el archivo de log si no existe
    os.makedirs(os.path.dirname(logfile), exist_ok=True)

    # Configurar el logger
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG if debug else logging.INFO)

    # Crear un manejador de archivo
    file_handler = logging.FileHandler(logfile)
    file_handler.setLevel(logging.DEBUG if debug else logging.INFO)

    # Crear un formateador y asignarlo al manejador
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    # Añadir el manejador al logger
    logger.addHandler(file_handler)

    return logger