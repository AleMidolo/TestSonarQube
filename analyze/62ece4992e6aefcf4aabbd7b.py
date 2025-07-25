def write_configuration(config_filename, rendered_config, mode=0o600, overwrite=False):
    """
    Dato un nome di file di configurazione di destinazione e un file YAML di configurazione renderizzato, scrivilo nel file.  
    Crea eventuali directory contenitrici, se necessario. Tuttavia, se il file esiste già e `overwrite` è impostato su `False`, interrompi l'operazione prima di scrivere qualsiasi cosa.
    """
    import os
    import pathlib

    # Convert path to Path object
    config_path = pathlib.Path(config_filename)
    
    # Check if file exists and overwrite is False
    if config_path.exists() and not overwrite:
        return
        
    # Create parent directories if they don't exist
    config_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Write the configuration file with specified mode
    with open(config_path, 'w') as f:
        f.write(rendered_config)
    
    # Set file permissions
    os.chmod(config_path, mode)