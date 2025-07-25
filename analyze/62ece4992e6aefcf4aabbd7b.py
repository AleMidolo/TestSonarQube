def write_configuration(config_filename, rendered_config, mode=0o600, overwrite=False):
    """
    Dado un nombre de archivo de configuración de destino y un archivo YAML de configuración renderizado, escríbelo en el archivo.  
    Crea cualquier directorio contenedor según sea necesario. Pero si el archivo ya existe y `overwrite` es `False`, aborta antes de escribir cualquier cosa.
    """
    import os
    import pathlib

    # Get directory path from config filename
    config_dir = os.path.dirname(config_filename)

    # Create directories if they don't exist
    if config_dir:
        pathlib.Path(config_dir).mkdir(parents=True, exist_ok=True)

    # Check if file exists and overwrite flag
    if os.path.exists(config_filename) and not overwrite:
        raise FileExistsError(f"Configuration file {config_filename} already exists and overwrite=False")

    # Write the configuration file with specified mode
    with open(config_filename, 'w') as f:
        f.write(rendered_config)
    
    # Set file permissions
    os.chmod(config_filename, mode)