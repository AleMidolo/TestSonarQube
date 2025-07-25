import os
import yaml

def write_configuration(config_filename, rendered_config, mode=0o600, overwrite=False):
    """
    Dado un nombre de archivo de configuración de destino y un archivo YAML de configuración renderizado, escríbelo en el archivo.  
    Crea cualquier directorio contenedor según sea necesario. Pero si el archivo ya existe y `overwrite` es `False`, aborta antes de escribir cualquier cosa.
    """
    # Check if the file already exists and overwrite is False
    if os.path.exists(config_filename) and not overwrite:
        return
    
    # Create the directory if it doesn't exist
    os.makedirs(os.path.dirname(config_filename), exist_ok=True)
    
    # Write the rendered config to the file
    with open(config_filename, 'w') as config_file:
        yaml.dump(rendered_config, config_file, default_flow_style=False)
    
    # Set the file permissions
    os.chmod(config_filename, mode)