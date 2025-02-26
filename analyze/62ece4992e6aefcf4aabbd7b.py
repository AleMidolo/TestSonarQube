import os
import yaml

def write_configuration(config_filename, rendered_config, mode=0o600, overwrite=False):
    """
    Dado un nombre de archivo de configuración de destino y un archivo YAML de configuración renderizado, escríbelo en el archivo.  
    Crea cualquier directorio contenedor según sea necesario. Pero si el archivo ya existe y `overwrite` es `False`, aborta antes de escribir cualquier cosa.
    """
    # Verificar si el archivo ya existe
    if not overwrite and os.path.exists(config_filename):
        raise FileExistsError(f"El archivo {config_filename} ya existe y overwrite es False.")
    
    # Crear el directorio contenedor si no existe
    os.makedirs(os.path.dirname(config_filename), exist_ok=True)
    
    # Escribir el archivo de configuración
    with open(config_filename, 'w') as config_file:
        yaml.dump(rendered_config, config_file)
    
    # Cambiar los permisos del archivo
    os.chmod(config_filename, mode)