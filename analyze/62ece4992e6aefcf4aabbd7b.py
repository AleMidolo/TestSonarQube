import os
import pathlib

def write_configuration(config_filename, rendered_config, mode=0o600, overwrite=False):
    """
    Dado un nombre de archivo de configuración de destino y un archivo YAML de configuración renderizado, escríbelo en el archivo.
    Crea cualquier directorio contenedor según sea necesario. Pero si el archivo ya existe y `overwrite` es `False`, aborta antes de escribir cualquier cosa.
    """
    # Convertir el nombre del archivo a un objeto Path
    config_path = pathlib.Path(config_filename)
    
    # Verificar si el archivo ya existe y si no se debe sobrescribir
    if config_path.exists() and not overwrite:
        return
    
    # Crear el directorio contenedor si no existe
    config_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Escribir el contenido renderizado en el archivo
    with open(config_path, 'w') as config_file:
        config_file.write(rendered_config)
    
    # Establecer los permisos del archivo
    os.chmod(config_path, mode)