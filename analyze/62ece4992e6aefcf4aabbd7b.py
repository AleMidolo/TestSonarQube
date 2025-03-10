import os
import yaml

def write_configuration(config_filename, rendered_config, mode=0o600, overwrite=False):
    """
    Dado un nombre de archivo de configuración de destino y un archivo YAML de configuración renderizado, escríbelo en el archivo.  
    Crea cualquier directorio contenedor según sea necesario. Pero si el archivo ya existe y `overwrite` es `False`, aborta antes de escribir cualquier cosa.
    """
    if os.path.exists(config_filename) and not overwrite:
        return
    
    os.makedirs(os.path.dirname(config_filename), exist_ok=True)
    
    with open(config_filename, 'w') as config_file:
        yaml.dump(rendered_config, config_file, default_flow_style=False)
    
    os.chmod(config_filename, mode)