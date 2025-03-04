def write_configuration(config_filename, rendered_config, mode=0o600, overwrite=False):
    import os
    import pathlib

    # Convert path to Path object
    config_path = pathlib.Path(config_filename)
    
    # Check if file exists and overwrite is False
    if config_path.exists() and not overwrite:
        return
        
    # Create parent directories if they don't exist
    config_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Write the configuration file
    with open(config_path, 'w') as f:
        f.write(rendered_config)
    
    # Set file permissions
    os.chmod(config_path, mode)